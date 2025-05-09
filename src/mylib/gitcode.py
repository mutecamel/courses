import os
from pathlib import Path
from typing import Iterable

import git
import orjson
import requests
from dotenv import load_dotenv
from git.util import rmtree
from requests.adapters import HTTPAdapter
from urllib3.util import Retry

load_dotenv()


gitcode_token = os.getenv("GITCODE_TOKEN")
assert gitcode_token, (
    "请先访问 https://gitcode.com/setting/token-classic 申请访问令牌，"
    "然后在 .env 文件里设置环境变量 GITCODE_TOKEN"
)

http_client = requests.Session()
retries = Retry(
    total=5,
    backoff_factor=1,
    status_forcelist=[400, 502, 503, 504],
    allowed_methods={"GET", "POST"},
)
http_client.mount("https://", HTTPAdapter(max_retries=retries))


def read_latest_update_ts() -> str | None:
    path = Path("gitcode/pulls")
    if not path.exists():
        return
    ts = max(
        (orjson.loads(f.read_bytes())["updated_at"] for f in path.glob("*/*-pr*.json")),
        default=None,
    )
    return ts


def pulls(*, incremental: bool = False, page_size: int = 100) -> Iterable[dict]:
    page_size = min(100, max(5, page_size))
    repos = [f"week{i + 1:02}" for i in range(16)] + ["courses"]
    base_url = "https://api.gitcode.com/api/v5/repos/cueb-fintech/{repo}/pulls"
    for repo in repos:
        params = {
            "access_token": gitcode_token,
            "sort": "updated",
            "direction": "asc",
            "since": "2025-01-01T00:00:00+08:00",
            "per_page": page_size,
            "page": 1,
        }
        if incremental and (latest := read_latest_update_ts()):
            params["since"] = latest
        while True:
            print(f"请求 pulls, {repo}，第 {params['page']} 页")
            resp = http_client.get(
                base_url.format(repo=repo),
                params=params,
            )
            if not (data := resp.json()):
                break
            yield from data
            if len(data) < page_size:
                break
            params["page"] += 1


def load_pulls(refresh: bool = True) -> None:
    assert Path.cwd().name == "courses"
    base_dir = Path("homework/pulls")
    if refresh:
        rmtree(base_dir)
    for d in pulls(incremental=not refresh):
        user = d["user"]["login"]
        repo = d["base"]["repo"]["path"]
        number = d["number"]
        path: Path = base_dir / user / f"{repo}-pr{number}.json"
        print(repo, d["updated_at"], user, f"pr{number}")
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(orjson.dumps(d, option=orjson.OPT_INDENT_2))
        if "repo" not in d["head"]:
            continue
        repo_dir: Path = base_dir / user / d["head"]["repo"]["path"]
        if repo_dir.exists():
            repo = git.Repo(repo_dir)
            repo.remotes.origin.pull()
        else:
            repo_url: str = d["head"]["repo"]["html_url"]
            repo = git.Repo.clone_from(repo_url, repo_dir)

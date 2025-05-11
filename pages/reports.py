import marimo

__generated_with = "0.13.6"
app = marimo.App(width="medium")


@app.cell
def _(mylib):
    cohort_data = mylib.manage.read_cohort_members()
    cohort_names = cohort_data["班级名称"].unique().sort().to_list()
    return cohort_data, cohort_names


@app.cell
def _(cohort_names, mo):
    sel_cohort_name = mo.ui.dropdown(
        label="选择班级: ",
        options=cohort_names,
        allow_select_none=False,
        value=cohort_names[0],
    )
    sel_cohort_name
    return (sel_cohort_name,)


@app.cell
def _(Path, math, orjson, pl, re):
    def get_weekly_data_record_item(username: str, i: int) -> float | None:
        base_dir = Path(f"homework/weekly/{username}")
        if not base_dir.exists():
            return
        n = max(
            [
                int(re.fullmatch(r"week\d\d-pr(\d+)\.json", f.name).group(1))
                for f in base_dir.glob(f"week{i:02}-pr*.json")
            ],
            default=None,
        )
        if n is None:
            return
        f = base_dir / f"week{i:02}-pr{n}.json"
        d = orjson.loads(f.read_bytes())
        if "repo" not in d["head"]:
            return
        repo = base_dir / d["head"]["repo"]["path"]
        n = sum(f.stat().st_size for f in repo.glob("**/*") if f.is_file())
        n = math.log(n)
        return n


    def get_weekly_data_record(username: str) -> pl.DataFrame:
        base_dir = Path(f"homework/weekly/{username}")
        df = pl.select(
            用户名=pl.lit(username, pl.String),
            week=pl.int_range(1, 17),
        )
        df = df.with_columns(
            score=pl.col("week").map_elements(
                lambda i: get_weekly_data_record_item(username, i),
                return_dtype=pl.Float64,
            )
        )
        return df


    def get_weekly_data(members_data: pl.DataFrame) -> pl.DataFrame:
        df = pl.concat(
            [
                get_weekly_data_record(username)
                for username in members_data["用户名"]
            ]
        )
        df = df.select(
            "用户名",
            "week",
            得分=((pl.col.score - 10) / (pl.col.score.max() - 10) * 20 + 80).over(
                "week"
            ),
        )
        df = df.sort("用户名", "week")
        df = df.group_by("用户名").agg(
            pl.col("得分").fill_null(70),
        )
        df = members_data.join(df, on="用户名", how="left")
        df = df.with_columns(
            得分=pl.col("得分").fill_null([70] * 16),
        )
        return df
    return (get_weekly_data,)


@app.cell
def _(cohort_data, get_weekly_data, pl, sel_cohort_name):
    cohort_name = sel_cohort_name.value
    if cohort_name:
        members_data = cohort_data.filter(pl.col("班级名称") == cohort_name)
    else:
        members_data = cohort_data

    weekly_data = get_weekly_data(members_data)
    return (weekly_data,)


@app.cell
def _(weekly_data):
    weekly_data.with_row_index("序号", 1).style.fmt_nanoplot(
        columns="得分",
        plot_type="line",
        autoscale=True,
    )
    return


@app.cell
def _():
    import re
    import math
    from pathlib import Path

    import orjson
    import marimo as mo
    import polars as pl

    import mylib.manage
    return Path, math, mo, mylib, orjson, pl, re


if __name__ == "__main__":
    app.run()

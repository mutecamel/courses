import io
from pathlib import Path
from typing import Literal

import polars as pl

assert Path.cwd().name == "courses"


base_dir = Path("user")


def read_tsv(fp: Path) -> pl.DataFrame:
    df = pl.read_csv(
        fp,
        separator="\t",
        encoding="utf8",
        infer_schema=False,
        raise_if_empty=False,
    )
    return df


def write_tsv(df: pl.DataFrame, fp: Path) -> None:
    df.write_csv(
        fp,
        separator="\t",
        line_terminator="\r\n",
    )


def to_display(df: pl.DataFrame) -> pl.DataFrame:
    if df.is_empty():
        df = pl.from_records([["没有数据"] * df.width], schema=df.columns, orient="row")
        df = df.with_row_index("序号", 0)
    else:
        df = df.with_row_index("序号", 1)
    df = df.with_columns(
        序号=pl.col("序号").cast(pl.String),
    )
    df = df.with_columns(
        pl.selectors.string().replace({None: "(无)"}),
    )
    return df


schema_cohort_members = pl.Schema(
    {
        "班级名称": pl.String,
        "学号": pl.String,
        "姓名": pl.String,
        "用户名": pl.String,
    }
)


def fp_cohort_members() -> Path:
    fp = base_dir / "cohort_members.csv"
    if not fp.exists():
        df = pl.DataFrame(schema=schema_cohort_members)
        write_tsv(df, fp)
    return fp


def read_cohort_members(display: bool = False) -> pl.DataFrame:
    fp = fp_cohort_members()
    df = read_tsv(fp)
    assert df.schema == schema_cohort_members
    d0 = df
    df = df.sort("班级名称", "学号")
    if not df.equals(d0):
        write_tsv(df, fp)
    if display:
        df = to_display(df)
    return df


schema_cohort_members_external = pl.Schema(
    {
        "学号": pl.String,
        "姓名": pl.String,
    }
)


def read_cohort_members_external_jwc(content: bytes) -> pl.DataFrame:
    f = io.BytesIO(content)
    df = pl.read_excel(
        f,
        read_options={
            "header_row": 4,
            "use_columns": "A,B",
            "dtypes": "string",
        },
    )
    return df


def read_cohort_members_external_gs(content: bytes) -> pl.DataFrame:
    f = io.BytesIO(content)
    df = pl.read_excel(
        f,
        read_options={
            "header_row": 3,
            "use_columns": "A,B",
            "dtypes": "string",
        },
    )
    return df


def read_cohort_members_external(
    content: bytes,
    file_type: Literal["jwc", "gs"],
    display: bool = False,
) -> pl.DataFrame:
    if file_type == "jwc":
        df = read_cohort_members_external_jwc(content)
    elif file_type == "gs":
        df = read_cohort_members_external_gs(content)
    else:
        raise NotImplementedError(file_type)
    assert df.schema == schema_cohort_members_external
    df = df.sort("学号")
    if display:
        df = to_display(df)
    return df


def update_cohort_members_replace(df: pl.DataFrame) -> None:
    d0 = read_cohort_members()
    df = df.drop("序号", strict=False)
    df = df.with_columns(
        pl.col("姓名").replace({"": None}),
    )
    (cohort_name,) = df["班级名称"].unique().to_list()
    d1 = d0.with_columns(
        班级名称=pl.col("班级名称").replace({cohort_name: None}),
    )
    d1 = d1.join(df, on="学号", how="full", coalesce=True).select(
        班级名称=pl.coalesce("班级名称_right", "班级名称"),
        学号=pl.col("学号"),
        姓名=pl.coalesce("姓名_right", "姓名"),
        用户名=pl.col("用户名"),
    )
    d1 = d1.sort("班级名称", "学号")
    if not d1.equals(d0):
        write_tsv(d1, fp_cohort_members())


def update_cohort_members_merge(df: pl.DataFrame) -> None:
    d0 = read_cohort_members()
    df = df.drop("序号", strict=False)
    df = df.with_columns(
        pl.col("姓名").replace({"": None}),
    )
    d1 = d0.join(df, on=["班级名称", "学号"], how="full", coalesce=True).select(
        班级名称=pl.col("班级名称"),
        学号=pl.col("学号"),
        姓名=pl.coalesce("姓名_right", "姓名"),
        用户名=pl.col("用户名"),
    )
    d1 = d1.sort("班级名称", "学号")
    if not d1.equals(d0):
        write_tsv(d1, fp_cohort_members())


def update_cohort_members(
    df: pl.DataFrame,
    method: Literal["replace", "merge"] = "replace",
) -> None:
    if method == "replace":
        update_cohort_members_replace(df)
    elif method == "merge":
        update_cohort_members_merge(df)
    else:
        raise NotImplementedError(method)


def read_cohort_overview(display: bool = False) -> pl.DataFrame:
    df = read_cohort_members()
    df = df.group_by("班级名称").agg(
        成员数量=pl.len(),
    )
    df = df.sort("班级名称")
    if display:
        df = to_display(df)
    return df


schema_usernames_external = pl.Schema(
    {
        "学号": pl.String,
        "用户名": pl.String,
    }
)


def read_usernames_external_wps(content: bytes) -> pl.DataFrame:
    f = io.BytesIO(content)
    df = pl.read_excel(
        f,
        read_options={
            "use_columns": "E,F",
            "dtypes": "string",
        },
    )
    df = df.rename(
        {
            "首经贸学号": "学号",
            "GitCode ID": "用户名",
        }
    )
    df = df.with_columns(
        学号=pl.col("学号").str.strip_chars(),
        用户名=pl.col("用户名").str.strip_chars().str.strip_prefix("@"),
    )
    return df


def read_usernames_external(
    content: bytes,
    file_type: Literal["wps"],
    display: bool = False,
) -> pl.DataFrame:
    if file_type == "wps":
        df = read_usernames_external_wps(content)
    else:
        raise NotImplementedError(file_type)
    assert df.schema == schema_usernames_external
    df = df.sort("学号")
    if display:
        df = to_display(df)
    return df


def update_usernames(df: pl.DataFrame):
    d0 = read_cohort_members()
    d1 = df.drop("序号", strict=False)
    d1 = d0.join(d1, on="学号", how="left")
    d1 = (
        d1.with_columns(
            pl.col("用户名").replace({"": None}),
            pl.col("用户名_right").replace({"": None}),
        )
        .with_columns(
            用户名=pl.coalesce("用户名_right", "用户名"),
        )
        .drop("用户名_right")
    )
    d1 = d1.sort("班级名称", "学号")
    if not d1.equals(d0):
        write_tsv(d1, fp_cohort_members())


schema_member_id = pl.Schema(
    {
        "Gitcode用户名": pl.String,
        "学号": pl.String,
    }
)


def fp_member_id() -> Path:
    fp = base_dir / "member_id.csv"
    if not fp.exists():
        df = pl.DataFrame(schema=schema_member_id)
        write_tsv(df, fp)
    return fp


def read_member_id() -> pl.DataFrame:
    fp = fp_member_id()
    df = read_tsv(fp)
    assert df.schema == schema_member_id
    return df

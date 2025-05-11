import marimo

__generated_with = "0.13.6"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # [金融 AI 编程实战](https://gitcode.com/cueb-fintech/courses) —— 后台管理

    > ### 曾用名：金融计算机语言、金融编程与计算、金融数据库
    > 
    > 持续建设中，欢迎参与添砖加瓦🌹
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""## 班级概览""")
    return


@app.cell(hide_code=True)
def _(btn_cohort_submit, btn_usernames_submit, mo, mylib):
    btn_cohort_submit
    btn_usernames_submit
    mo.ui.table(
        data=mylib.manage.read_cohort_overview(display=True),
        selection=None,
        show_column_summaries=False,
    )
    return


@app.cell(hide_code=True)
def _(mo, mylib):
    mo.md(f"""## 班级成员 ([`{mylib.manage.fp_cohort_members().as_posix()}`](vscode://file/{mylib.manage.fp_cohort_members().absolute().as_posix()}))""")
    return


@app.cell(hide_code=True)
def _(btn_cohort_submit, btn_usernames_submit, mo, mylib):
    btn_cohort_submit
    btn_usernames_submit
    cohort_members = mylib.manage.read_cohort_members(display=True)
    sel_cohort_name = mo.ui.dropdown(
        options=cohort_members["班级名称"].unique().sort(), label="选择班级"
    )
    sel_cohort_name
    return cohort_members, sel_cohort_name


@app.cell(hide_code=True)
def _(cohort_members, mo, pl, sel_cohort_name):
    _df = cohort_members
    if sel_cohort_name.value:
        _df = _df.filter(pl.col("班级名称") == sel_cohort_name.value)
    mo.ui.table(data=_df, selection=None, show_column_summaries="stats")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## 导入班级成员""")
    return


@app.cell(hide_code=True)
def _(mo):
    cohort_name = mo.ui.text(label="班级名称")
    cohort_file_type = mo.ui.dropdown(
        label="文件类型",
        options={"教务处系统导出": "jwc", "研究生院系统导出": "gs"},
    )
    cohort_file = mo.ui.file(label="选择文件", filetypes=[".xls", ".xlsx"])
    mo.hstack([cohort_file, cohort_file_type, cohort_name], justify="start")
    return cohort_file, cohort_file_type, cohort_name


@app.cell(hide_code=True)
def _(cohort_file, cohort_file_type, cohort_name, mo, mylib, pl):
    def read_cohort_members() -> pl.DataFrame | None:
        if (
            not cohort_name.value
            or not cohort_file_type.value
            or not cohort_file.value
        ):
            return
        df = mylib.manage.read_cohort_members_external(
            content=cohort_file.value[0].contents,
            file_type=cohort_file_type.value,
            display=True,
        )
        df = df.insert_column(
            1, pl.lit(cohort_name.value, pl.String).alias("班级名称")
        )
        return df


    cohort_data = read_cohort_members()
    (
        mo.md("填写以上表单以预览准备导入的数据")
        if cohort_data is None
        else mo.ui.table(
            label=f"预览数据: {cohort_file.value[0].name}",
            data=cohort_data,
            selection=None,
        )
    )
    return (cohort_data,)


@app.cell(hide_code=True)
async def _(asyncio, btn_cohort_submit, mo):
    async def show_cohort_submit_spinner():
        with mo.status.spinner(title="提交中...") as _spinner:
            await asyncio.sleep(1)
            _spinner.update("提交完成")
            await asyncio.sleep(1)


    await show_cohort_submit_spinner() if btn_cohort_submit.value else None
    return


@app.cell(hide_code=True)
def _(cohort_data, mo, mylib, pl):
    def btn_cohort_submit_on_change(value: bool) -> None:
        mylib.manage.update_cohort_members(
            df=cohort_data,
            method=rad_cohort_method.value,
        )


    rad_cohort_method = mo.ui.radio(
        label="更新数据: ",
        options={
            "合并": "merge",
            "替换": "replace",
        },
        value="合并",
        inline=True,
    )
    btn_cohort_submit = mo.ui.run_button(
        label="提交",
        kind="danger",
        disabled=not isinstance(cohort_data, pl.DataFrame),
        on_change=btn_cohort_submit_on_change,
    )
    mo.hstack([rad_cohort_method, btn_cohort_submit], justify="start")
    return (btn_cohort_submit,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## 导入 Gitcode 用户名""")
    return


@app.cell(hide_code=True)
def _(mo):
    usernames_file = mo.ui.file(label="选择文件", filetypes=[".xls", ".xlsx"])
    usernames_file_type = mo.ui.dropdown(
        label="文件类型",
        options={
            "金山 WPS 表单导出": "wps",
        },
    )
    mo.hstack([usernames_file, usernames_file_type], justify="start")
    return usernames_file, usernames_file_type


@app.cell(hide_code=True)
def _(mo, mylib, pl, usernames_file, usernames_file_type):
    def read_usernames() -> pl.DataFrame | None:
        if not usernames_file.value or not usernames_file_type.value:
            return
        df = mylib.manage.read_usernames_external(
            content=usernames_file.value[0].contents,
            file_type=usernames_file_type.value,
            display=True,
        )
        return df


    usernames_data = read_usernames()
    (
        mo.md("填写以上表单以预览准备导入的数据")
        if usernames_data is None
        else mo.ui.table(
            label=f"预览数据: {usernames_file.value[0].name}",
            data=usernames_data,
            selection=None,
        )
    )
    return (usernames_data,)


@app.cell(hide_code=True)
async def _(asyncio, btn_usernames_submit, mo):
    async def show_usernames_submit_spinner():
        with mo.status.spinner(title="提交中...") as _spinner:
            await asyncio.sleep(1)
            _spinner.update("提交完成")
            await asyncio.sleep(1)


    await show_usernames_submit_spinner() if btn_usernames_submit.value else None
    return


@app.cell(hide_code=True)
def _(mo, mylib, pl, usernames_data):
    def btn_usernames_submit_on_change(value: bool) -> None:
        mylib.manage.update_usernames(usernames_data)


    btn_usernames_submit = mo.ui.run_button(
        label="更新",
        kind="danger",
        disabled=not isinstance(usernames_data, pl.DataFrame),
        on_change=btn_usernames_submit_on_change,
    )
    btn_usernames_submit
    return (btn_usernames_submit,)


@app.cell(hide_code=True)
def _():
    import asyncio
    from pathlib import Path

    import marimo as mo
    import polars as pl

    import mylib.manage
    return asyncio, mo, mylib, pl


if __name__ == "__main__":
    app.run()

import polars as pl
from pathlib import Path

def clean_xiangcai(file_path: Path) -> pl.DataFrame:
    # 1. 读取为字符串
    df = pl.read_csv(
        file_path,
        separator="\t",
        encoding="gb18030",
        infer_schema=False
    )
    # 2. 基本清洗
    df = (
        df
        # 转日期、时间
        .with_columns([
            pl.col("发生日期").str.strptime(pl.Date, "%Y-%m-%d"),
            pl.col("成交时间").str.strptime(pl.Time, "%H:%M:%S")
        ])
        # 去掉 ="000900" 里多余字符
        .with_column(
            pl.col("证券代码").str.replace_all(r'="?(\d+)"?', r'\1')
        )
        # 只保留买入/卖出
        .filter(pl.col("业务名称").is_in(["证券买入", "证券卖出"]))
    )
    # 3. 数值列统一转换
    for col in ["成交数量", "成交价格", "成交金额", "手续费", "印花税", "过户费", "其他费", "发生金额"]:
        df = df.with_column(pl.col(col).cast(pl.Float64))
    # 4. 添加券商字段
    df = df.with_column(pl.lit("湘财").alias("券商"))
    return df

# 批量处理所有“湘财”交割单
xiangcai_files = Path("./stock_trades").glob("*-湘财.xls")
d1 = pl.concat([clean_xiangcai(f) for f in xiangcai_files])

# 查看前几行
print(d1.head())
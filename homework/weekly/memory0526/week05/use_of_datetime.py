from datetime import date, datetime, timedelta  # noqa: F401

t1 = date.today()
t2 = date(2025, 11, 3)
td = t2 - t1
print(td, type(td))  ##看两个日期之间相差多少天
print(td.days)  ##查看属性


##字符串进行日期的计算
s1 = "2025-04-14"
s2 = "2025-11-03"
d1 = datetime.strptime(s1, "%Y-%m-%d")
d2 = datetime.strptime(s2, "%Y-%m-%d")
print(s1)
print(s2)
##可以通过查询python datetime format查询到不同的格式

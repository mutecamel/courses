from datetime import date, datetime, timedelta

# 获取当前日期
t1 = date.today()
print(t1)

# 创建指定日期对象
t2 = date(2025, 12, 25)
print(t2)

# 计算两个日期的时间差
td = t2 - t1
print(td)
print(type(td))
# 打印时间差的天数
print(td.days)

# 定义日期时间格式字符串
s = "2024-08-15"
# 将字符串解析为datetime对象
d1 = datetime.strptime(s, "%Y-%m-%d")
print(d1)

# 将datetime对象格式化为字符串
s2 = datetime.strftime(d1, "%Y-%m-%d")
print(s2)

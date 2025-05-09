from datetime import date, datetime

# 调用 date.today() 方法获取当前日期
t1 = date.today()
print(t1)
t2 = date(2024, 6, 11)
t = t2 - t1
print(t)
print(type(t))
print(t.days)

a = "2024-01-01"
b = "2025-01-01"
# 将字符串 a 转换为 datetime 对象
c = datetime.strptime(a, "%Y-%m-%d")
# 将字符串 b 转换为 datetime 对象
d = datetime.strptime(b, "%Y-%m-%d")
# 计算两个日期之间的时间差
diff = d - c
print(diff)
print(diff.days)
print(c)
print(d)

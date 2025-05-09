from datetime import date, datetime, timedelta  # noqa: F401

t1 = date.today()
t2 = date(2025, 9, 10)
t = t2 - t1
print(t)
print(type(t))
print(t.days)

m1 = "2024-09-10"
m2 = "2025-09-10"
n1 = datetime.strptime(m1, "%Y-%m-%d")  # 将字符串解析成日期时间的类型
n2 = datetime.strptime(m2, "%Y-%m-%d")
print(n1)
print(n2)

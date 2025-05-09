from datetime import date, datetime, timedelta  # noqa: F401

print(date.today())  #   2025-04-08

t1 = date.today()
t2 = date(2025, 11, 11)
print(t2 - t1)  #   217 days, 0:00:00
td = t2 - t1
print(td)
print(type(td))  #  <class 'datetime.timedelta'>
print(td.days)  # 217

s1 = "2024-03-30"
s2 = "2024-08-26"
d1 = datetime.strptime(s1, "%Y-%m-%d")
d2 = datetime.strptime(s2, "%Y-%m-%d")
print(d1)
print(d2)

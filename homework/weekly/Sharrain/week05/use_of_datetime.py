from datetime import date, datetime, timedelta  # noqa: F401

t1 = date.today()
t2 = date(2025, 11, 11)
td = t2 - t1
print(td)
print(type(td))
print(td.days)

s1 = "2025-05-23"
s2 = "2024-12-04"
d1 = datetime.strptime(s1, "%Y-%m-%d")
d2 = datetime.strptime(s2, "%Y-%m-%d")
print(d1)
print(d2)
breakpoint()

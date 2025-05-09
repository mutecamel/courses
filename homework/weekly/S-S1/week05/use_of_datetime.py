from datetime import date, datetime, timedelta  # noqa: F401

a = date.today()
aa = date(2025, 11, 11)
b = aa - a
print(b)
print(type(b))
print(b.days)

a = "2024-09-01"
aa = "2024-11-11"
b = datetime.strptime(a, "%Y-%m-%d")
bb = datetime.strptime(aa, "%Y-%m-%d")
print(b)
print(bb)
breakpoint()

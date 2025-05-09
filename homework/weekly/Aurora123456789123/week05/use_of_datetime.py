from datetime import date, datetime, timedelta  # noqa: F401

print(date.today())
t1 = date.today()
t2 = date(2014, 8, 10)
td = t1 - t2
print(type(td))
print(td.days)

s1 = "2012-04-08"
s2 = "2014-08-10"
d1 = datetime.strptime(s1, "%Y-%m-%d")
d2 = datetime.strptime(s2, "%Y-%m-%d")
print(d1)
print(d2)

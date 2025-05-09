from datetime import date

t1 = date.today()
t2 = date(2025, 11, 11)
td = t2 - t1
print(td)
print(type(td))
print(td, date)

s1 = "2024-06-15"
s2 = "2024-11-11"
d1 = date.strftime(s1, "%Y-%m-%d")
d2 = date.strftime(s2, "%Y-%m-%d")
print(d1)
print(d2)

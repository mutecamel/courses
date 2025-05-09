from datetime import date

print(date.today())

t1 = date.today()
t2 = date(2025, 10, 1)
td = t2 - t1
print(td)
print(td.days)

s1 = date(2024, 12, 31)
s2 = date(2025, 1, 3)
sd = s2 - s1
print(sd)

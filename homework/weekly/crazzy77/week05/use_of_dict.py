print("字面值")
a = {"f": 7, "g": 8, "j": 9}
print(a)
print(type(a))

for m in a:
    print(m)

for m in a:
    print(a[m])

for m in a.values():
    print(a)

l = [m for m in a.items()]
print(l)

for k, v in a.items():
    print(k, v)

assert not {}

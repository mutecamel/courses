a = {"a": 5, "you": 49, "me": 999}
print(a)
print(type(a))

for b in a:
    print(b)

for b in a:
    print(a[b])

for b in a.values():
    print(b)

q = [b for b in a.items()]
print(q)

for c, d in a.items():
    print(c, d)

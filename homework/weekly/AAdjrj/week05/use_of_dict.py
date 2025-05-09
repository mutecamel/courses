d = {"a": 1, "bb": 5, "cat": 3}
print(d)
print(type(d))

for a in d:
    print(a)

for a in d:
    print(d[a])

for a in d.values():
    print(a)

l = [a for a in d.values()]
print(l)

d = {"a": 1, "bb": 5, "cat": 3}
print(d)
print(type(d))

for a in d:
    print(a)

for a in d:
    print(d[a])

for a in d.values():
    print(a)

f = [a for a in d.items()]
print(f)

for k, v in d.items():
    print(k, v)

breakpoint()

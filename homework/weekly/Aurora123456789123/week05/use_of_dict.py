d = {"Wendy": 3, "Shiho": 4, "Sherry": 8}
print(d)

for a in d:
    print(a)

for a in d:
    print(d[a])

for a in d.values():
    print(a)

l = [a for a in d.items()]
print(l)

for k, v in d.items():
    print(k, v)

breakpoint()

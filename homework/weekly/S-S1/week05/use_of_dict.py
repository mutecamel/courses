d = {"p": 22, "pad": 66, "caper": 99}
print(d)
print(type(d))


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

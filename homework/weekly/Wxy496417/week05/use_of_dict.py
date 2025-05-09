d = {"lili": 163, "cherry": 168, "jack": 188}
print(d)
print(type(d))
print(len(d))

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

try:
    assert {}
except AssertionError as e:
    print(type(e))

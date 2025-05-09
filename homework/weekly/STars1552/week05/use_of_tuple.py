t = (1, "a", 3.14)
print(t)
print(type(t))

print(t[0])
print(t[1])
print(t[2])

try:
    t[0] = 9
except TypeError as e:
    print(e)

d = {}
d["abc"] = 5
d[7] = 100
print(d)

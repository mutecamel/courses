t = ("1", "a", 3.14)
print(type(t))
print(t)

print(len(t))
print(t[0])
print(t[1])
print(t[2])

try:
    t[0] = 7
except TypeError as e:
    print(e)

d = {}
d["aaa"] = 1
d[3] = 5
q = [3, 1]

try:
    d[q] = 2
except TypeError as e:
    print(e)
print(d)

t = (3, 1)
d[t] = 2
print(d)
print(d[3, 1])

t = 1, 2, 3.14
print(t)
print(type(t))

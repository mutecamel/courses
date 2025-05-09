t = (1, "a", 3.14)
print(t)
print(type(t))

print(t[0])
print(t[1])
print(t[2])

try:
    t[0]
except TypeError as e:
    print(e)

d = {}
d["abc"] = 5
d[7] = 100
q = [3, 1]

try:
    d[q] = 21
except TypeError as e:
    print(e)

t = (3, 1)
d[t] = 21
print(d)
print(d[3, 1])

t = 1, 4, 0, 2
print(t)
print(type(t))

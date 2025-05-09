t = (2, "abx", 7.14)
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
d[7] = 122
print(d)

q = [3.1]
try:
    d[q] = 32
except TypeError as e:
    print(e)

t = (2, 4)
d[t] = 24
print(d)
print(d[2, 4])


t = 2, 3, 5, 1
print(t)

a = (1, "b", 33669)
print(a)
print(type(a))

print(a[0])
print(a[1])
print(a[2])

try:
    a[0] = 20
except TypeError as e:
    print(e)

d = {}
d["abc"] = 5
d[77] = 20177
q = [5, 992]

try:
    d[q] = 443
except TypeError as e:
    print(e)

dd = (3, 1)
d[dd] = 366
print(d)
print(d[3, 1])

aaa = 2, 4, 7, 271
print(aaa)
print(type(aaa))

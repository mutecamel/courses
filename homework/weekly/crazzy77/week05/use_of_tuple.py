print("字面值")
a = (3, "asd", 5.77)
print(type(a))
print(a)

print(a[0])
print(a[1])
print(a[2])

try:
    a[1] = 9
except TypeError as e:
    print(e)


d = {}
d["abc"] = 9
d[8] = 200
q = [2, 5]

try:
    d[q] = 32
except TypeError as e:
    print(e)

t = (5, 8)
d[t] = 32
print(d)
print(d[5, 8])

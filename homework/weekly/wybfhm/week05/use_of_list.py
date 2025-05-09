l = [1, 5, "abc"]
print(l)

print(l[0])
print(l[1])
print(l[2])

print(l[-1])
print(l[-1][1])

a = [2, 5]
b = ["ac"]
print(a + b)
print(b + a)

a = [2, 5]
b = [5]
try:
    print(a - b)
except TypeError as e:
    print(e)

a = [2, 5]
print(a * 3)

a = [2, 5]
b = a * 3
print(f"{b=}")
a[0] = 9
print(a)
print(b)

a = [2, 5]
b = [a] * 3
print(f"{b=}")
a[0] = 9
print(a)
print(b)

a = [2, 5, 3]
b = [i**2 for i in a]
print(b)
b = [i**2 for i in a if i < 4]
print(b)

a = [2, 5]
b = [a] * 3
print(f"{b=}")
x = a.append(4)
print(x)
print(a)
print(b)

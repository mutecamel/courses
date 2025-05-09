l = [1, 2, "qwe"]
print(l)

print(l[0])
print(l[1])
print(l[2])

try:
    print(l[3])
except IndexError as e:
    print(e)

print(l[-1])
print(l[-1][1])

a = [2, 6]
b = ["a", "d"]
print(a + b)
print(b + a)
print(a + b == b + a)

a = [2, 8]
b = [9]
try:
    print(a - b)
except TypeError as e:
    print(e)

a = [2, 4]
print(a * 3)

a = [2, 6]
b = a * 2
print(f"{b=}")
a[0] = 4
print(a)
print(b)

a = [2, 8]
b = [a] * 8
print(f"{b=}")
a[0] = 9
print(a)
print(b)

a = [3, 6, 9]
b = [i**2 for i in a]
print(b)
b = [i**3 for i in a if i > 4]
print(b)

a = [2, 6]
b = a * 2
print(f"{b=}")
x = a.append(4)
print(a)
print(b)
print(x)

l = [1, "badui", 3]
print(l)

print(l[0])
print(l[1])
print(l[2])

try:
    print(l[3])
except IndexError as e:
    print(e)

print(l[-2])
print(l[-2][1])

a = [3, 9]
b = ["a", "d"]

print(a + b)
print(b + a)
print(a + b == b + a)

a = [3, 9]
b = [7]
try:
    print(a - b)
except TypeError as e:
    print(e)

a = [3, 9]
print(a * 3)

a = [3, 9]
b = a * 3
a[0] = 10
print(a)
print(b)

a = [2, 9, 200]
b = [i**2 for i in a]
print(b)
b = [i**2 for i in a if i < 66]
print(b)

a = [3, 9]
b = a * 3
x = a.append(8)
print(x)
print(a)
print(b)

breakpoint()

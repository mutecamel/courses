l = [3, 4, "Wendy", "Shiho"]
print(l)

print(l[2])
try:
    print(l[4])
except IndexError as e:
    print(e)

print(l[3][0])

print(l[2][:-1])

a = ["Sherry", "Shiho"]
b = [26, 4869]
print(a + b)
print(b + a)
print(a + b == b + a)
try:
    print(a * b)
except TypeError as e:
    print(e)

a = [3, 4]
print(a * 9)
b = a * 3
a[0] = 10
print(a, b)
print(f"{b=}")

a = [3, 4]
print(a * 9)
b = [a] * 3
a[0] = 10
x = a.append(8)
print(a, b)
print(f"{b=}")

a = [1, 2, 3]
b = [i**2 for i in a]
print(b)

breakpoint()

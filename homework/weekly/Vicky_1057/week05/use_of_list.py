f = [1, 5, "abc"]
print(f)

print(f[0])
print(f[1])
print(f[2])

try:
    print(f[3])
except IndexError as e:
    print(e)

print(f[-1])
print(f[-1][1])

a = [2, 5]
b = ["a", "c"]
print(a + b)
print(b + a)
print(a + b == b + a)

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

a = [2, 5, 3]
b = [i**2 for i in a]  # 推导式
print(b)
b = [i**2 for i in a if i < 4]
print(b)

a = [2, 5]

l = [1, 5, "abc"]
print(1)
print(1[0])
print(1[1])
print(1[2])

try:
    print(1[3])
except IndexError as e:
    print(e)

print(1[-1])
print(1[-1][1])

a = [2, 5]
b = [5]
try:
    print(a - b)
except TypeError as e:
    print(e)

a = [2, 5]
b = a = 3
print(f"{b=}")
a[0] = 9
print(a)
print(b)

a = [2, 5]
b = [a] = 3
print(f"{b=}")
a[0] = 9
print(a)
print(b)

a = [2, 5]
b = a * 3
print(f"{b=}")
x = a.append(4)
print(x)
print(a)
print(b)

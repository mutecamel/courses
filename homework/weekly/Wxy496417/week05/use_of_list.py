l1 = [1, 3, 4]
l2 = [1, 2, 3, "abc", "你好"]
print(l1, l2)

print(l1[0])
print(l1[1])
print(l1[2])
print(l2[3])
print(l2[4])

try:
    l2[5]
except IndexError as e:
    print(e)


print(l1[-1])
print(l2[-2][1])
print(l2[-1][1])

a = [1, 5]
b = ["a", "b"]
print(a + b)
print(b + a)
print(a + b == b + a)

a = [1, 2, 3]
b = [1, 2]
try:
    a - b
except TypeError as e:
    print(e)

print(b * 2)

a = [1, 2]
b = a * 3
a[0] = 7
print(a)
print(b)

a = [1, 2]
b = [a] * 3
print(f"{b=}")
a[0] = 7
print(a)
print(b)

a = [1, 2, 3]
b = [i**2 for i in a]
print(b)
c = [i + 2 for i in a]
print(c)
c = [i + 2 for i in a if i < 3]
print(c)

a = [1, 2]
b = [a] * 3
print(f"{b=}")
x = a.append(4)
print(x)
print(a)
print(b)

print(len(b))
breakpoint()

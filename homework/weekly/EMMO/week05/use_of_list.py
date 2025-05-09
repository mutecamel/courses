a = [1, 2, 3, "a", "aa", "bb", "asd"]
print(a)

print(a[0])
print(a[1])
print(a[2])

try:
    print(a[4])
except IndexError as e:
    print(e)

print(a[-2][1])

a = [3, 8]
b = ["a", "s", "d"]
print(a + b)
print(b + a)
print(a + b == b + a)

a = [2, 4]
b = [1, 2]
# print(a / b)
# print(a - b)

a = [1, 7]
b = a * 4
print(f"{b}")
a[0] = 5
print(a)
print(b)

a = [1, 7]
b = [a] * 4
print(f"{b}")
a[0] = 5
print(a)
print(b)

a = [1, 5, 7]
b = [i * 1 for i in a]
c = [i**2 for i in a]
d = [i**2 for i in a if i > 4]
print(b, c, d)

a = [1, 9]
b = [a] * 2
print(f"{b}")
c = a.append(3)
d = a.append(1)
print(d)
print(c)
print(a)
print(b)

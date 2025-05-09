print("字面值")
a = [2, 5, "ghjk"]
print(a)

print(a[0])
print(a[1])
print(a[2])
print(a[-1])
print(a[-1][2])

try:
    print(a[3])
except IndexError as e:
    print(e)

a = [2, 5]
b = [5, 2]
print(a + b)
print(b + a)
print(b + a == a + b)

a = [8, 9]
b = [9]
try:
    print(a - b)
except TypeError as e:
    print(e)

a = [3, 8]
print(a * 4)

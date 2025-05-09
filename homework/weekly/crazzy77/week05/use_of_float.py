import random

print("字面值")
x = 5.78
print(type(x))

print("初始化")
y = float("5.78")
print(type(y))

assert x == y

x = 6 / 7
print(x, type(x))

x = random.random()
print(x)

assert not 0.0

s = float("nan")
print(s + 10)
print(s > 10)
print(s < 10)
print(s == 10)

a = float("inf")
print(3.14e2)
print(a > 10e100)
print(a > a)
print(a == a)

b = float("-inf")
print(b)
print(b > b)
print(b == b)

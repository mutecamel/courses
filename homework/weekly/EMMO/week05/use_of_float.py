import random

a = 3.1415926
b = 1.23
print(type(a))
print(type(b))
c = float("1.2")
print(type(c))
d = 7 / 6
print(d, type(d))

x = random.random()
print(x)

x = 0
print(type(x))

y = 1
print(type(y))

s = float("nan")  # nan是缺失值，无法比较大小，且无论怎么运算都是nan，是浮点数
print(type(s))
print(s + 3)
print(s * 5)

p = float("inf")  # inf为正无穷，大于任何浮点数（除了自己）
print(p)
print(p < 999999999999999999999)

q = float("-inf")
print((-q) == p)

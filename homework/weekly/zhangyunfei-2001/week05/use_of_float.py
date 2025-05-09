import random

x = 3.14159
print(type(x))


y = float("3.14159")
print(type(y))
assert x == y


x = 10 / 3
print(x, type(x))

x = random.random()
print(x)

assert not 0.0

f = float("nan")  ##特殊值
print(f)

print(3.14e2)  ##3.14乘10的平方
inf = float("inf")
print(inf == inf)  ##正无穷等于正无穷
##浮点数不精确，支持各种运算

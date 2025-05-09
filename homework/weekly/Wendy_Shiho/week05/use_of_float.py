import random

x = 3.14
print(type(x))

y = float("3.14")
print(type(y))

assert x == y

x = 7 / 3
print(x, type(x))

x = random.random()
print(x)

nan = float("nan")
print(nan * 2)
print(nan >= 2)

pinf = float("inf")
print(3.14e2)
print(pinf > 1e200)

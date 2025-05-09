import random

x = 3.1415
print(type(x))

y = float(3.1415)
print(type(y))

assert x == y

x = 11 / 3
print(x, type(x))

x = random.random()
print(x)

assert not 0.0
nan = float("nan")
print(nan + 10)
print(nan > 31)
print(nan < 31)
print(nan == 31)

pinf = float("inf")
print(3.14e3)
print(pinf > 2e100)
print(pinf > pinf)
print(pinf == pinf)

ninf = float("-inf")
print(ninf)

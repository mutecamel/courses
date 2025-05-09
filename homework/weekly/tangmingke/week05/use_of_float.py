import random

x = 3.14
print(type(x))

y = float("3.14")
print(type(y))

assert x == y

x = 5 / 3
print(x, type(x))

x = random.random
print(x)

assert 0.0

nan = float("nan")
print(nan + 3)
print(nan > 3)
print(nan < 3)
print(nan == 3)

pinf = float("inf")
print(3.14e-2)
print(pinf > 1e200)
print(pinf > pinf)
print(pinf == pinf)

ninf = float("-inf")
print(ninf)
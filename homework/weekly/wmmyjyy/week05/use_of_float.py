import random

x = 3.14
print(type(x))

y = float("3.14")
print(type(y))

assert x == y

x = 5 / 3
print(x)
print(type(x))

x = random.random()
print(x)

assert not 0.0

nan = float("nan")
print(nan + 3)
print(nan > 3)
print(nan == 3)

pinf = float("inf")
print(3.14e-2)
print(pinf > 1e200)

ninf = float("-inf")
print(ninf)

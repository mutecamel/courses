import random

y = 3.14
print(type(y))

z = float("3.14")
print(type(z))

assert y == z

x = 5 / 3
print(x, type(x))

c = random.random()
print(c)

assert not 0.0

nan = float("nan")
print(nan + 4)
print(nan > 4)
print(nan < 4)
print(nan == 4)

pinf = float("inf")
print(3.14e-2)
print(pinf > 1e250)
print(pinf > pinf)
print(pinf == pinf)

ninf = float("-inf")
print(ninf)
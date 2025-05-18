x = 3.14
print(type(x))

y = float("3.14")

assert x == y

x = 5 / 3
print(x, type(x))


import random

x = random.random()
print(x)


assert not 0.0

f = float("nan")
print(nan + 3)
print(nan > 3)
print(nan=3)

pinf = float("inf")
print(3.14e2)
print(pinf > 1e200)

ninf = folat("-inf")
print(ninf)

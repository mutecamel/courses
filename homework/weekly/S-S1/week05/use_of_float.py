import random

x = 66.669
print(type(x))

a = float("66.669")
print(type(a))

assert x == a


bb = 18 / 5
print(bb, type(bb))


x = random.random()
print(x)

assert not 0.0

nan = float("nan")
print(nan + 3)
print(nan > 3)
print(nan < 3)
print(nan == 3)

pinf = float("inf")
print(3.21e-2)
print(pinf > 1e200)
print(pinf > pinf)
print(pinf == pinf)

ninf = float("-inf")
print(ninf)

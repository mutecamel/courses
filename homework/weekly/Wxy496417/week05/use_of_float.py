import random

a = 3.14
print(type(a))

b = "3.14"
print(type(b))
c = float("3.14")
print(type(c))

assert a == c

x = 7 / 3
print(x, type(x))

y = random.random()
print(y)

assert not 0.0

nan = float("nan")
print(nan + 3)
print(nan > 3)
print(nan < 3)
print(nan == 3)

pinf = float("inf")
print(1e200)
print(pinf > 1e200)
print(pinf == pinf)

ninf = float("-inf")
print(ninf)
print(ninf < -1e200)

a = 1.1
b = 1.2
x = a + b
y = a - b
z1 = a * b
z2 = b / a
z2 = b // a
z3 = b % a
print(x, y, z1, z2, z3)

try:
    a @ b
except TypeError as e:
    print(e)

x = 3.14
try:
    for c in x:
        print(c)
except TypeError as e:
    print(e)

try:
    len(x)
except TypeError as e:
    print(e)

try:
    x[0]
except TypeError as e:
    print(e)

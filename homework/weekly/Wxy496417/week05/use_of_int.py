a = 3
b = 6
c = 9
x = a + b
y = a * c
z1 = c / a
z2 = c / 1
print(x, y, z1, z2)
z3 = c // b
print(z3)
assert z3 == 1
z4 = c % b
assert z4 == 3
print(z4)
try:
    a @ b
except TypeError as e:
    print(e)

assert 3.2
try:
    assert 0
except AssertionError as e:
    print(type(e))

breakpoint()

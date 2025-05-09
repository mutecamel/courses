i = 123
x = 456
y = 789
z = x * y
print(z)

x = 78
y = 12
assert x // y == 6
assert x % y == 6

assert 123
try:
    assert 0
except AssertionError as e:
    print(type(e))

s = 7293

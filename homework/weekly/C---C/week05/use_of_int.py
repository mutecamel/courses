i = 42
a = 5
b = 7
z = a + b

x = 5
y = 17
assert y // x == 3
assert y % x == 2

assert 5

try:
    assert 0
except AssertionError as e:
    print(type(e))

x = 63323534
breakpoint()

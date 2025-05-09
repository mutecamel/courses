i = 43
x = 5
y = 7
z = x + y

x = 5
y = 23
assert y // x == 4
assert y % x == 3

assert 5

try:
    assert 0
except AssertionError as e:
    print(type(e))

breakpoint()

i = 42
x = 5
y = 17
z = x + y

assert y // x == 3
assert y % x == 2

assert 5
# assert 0  这个会报错
try:
    assert 0
except AssertionError as e:
    print(type(e))

breakpoint()

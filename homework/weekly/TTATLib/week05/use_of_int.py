i = 42
x = 8
y = 5
z = x + y


x = 5
y = 17
assert  y // x == 3
assert y % x == 2

assert 5

try:
    assert 0
except AssertionError as e:
    print(type(e))

x = 65535  
breakpoint()
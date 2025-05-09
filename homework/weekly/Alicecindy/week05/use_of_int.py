i = 82
x = 72
y = 100
z = x + y

x = 3
y = 11
assert y//x == 3
assert y%x ==2
 
assert 18

try:
    assert 0
except AssertionError as e:
    print(type(e))

x = 65534
breakpoint()

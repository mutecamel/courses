i = 22
x = 33
y = 44
z = (i + x) * y
print(z)  # 2420

x = 8
y = 19
assert y // x == 2  # 整除
assert y % x == 3  # 余除
x = 8
y = 24
assert y // x == 3

assert 8888

try:
    assert 0
except AssertionError as e:
    print(type(e))  # <class 'AssertionError'>

x = 10086

q = ["123", "234", "345", "456"]
print(":".join(q))  #   123:234:345:456
s = "123:234:345:456"
print(s.split(":"))  #   ['123', '234', '345', '456']
assert s.partition(":") == (
    "123",
    ":",
    "234:345:456",
)

breakpoint()

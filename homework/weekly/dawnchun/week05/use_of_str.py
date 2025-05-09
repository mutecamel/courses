a = [2, 5]
b = [2, 5]
x = id(a)
y = id(b)
print(x)
print(y)
a[0] = 9
print(a)
print(b)
print(id(a))
print(id(b))
print(type(a))
print(isinstance(a, str))
print(isinstance(a, list))
print(isinstance(a, (str, float)))
try:
    assert isinstance(a, str)
except AssertionError:
    print("type error")
print("goodbye")

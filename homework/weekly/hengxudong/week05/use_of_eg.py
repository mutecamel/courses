a = [2, 5]
b = [2, 5]
x = id(a)
print(x)
y = id(b)
print(y)
a[0] = 9
print(a)
print(b)
print(id(a))
print(id(b))
print(type(a))
print(isinstance(a, str))
print(isinstance(a, list))
print(dir(a))
print(str(a))
print(isinstance(a, (str, list)))
print(isinstance(a, (str, float)))
try:
    assert isinstance(a, str)
except AssertionError:
    breakpoint()
    print("type error")
print("good")

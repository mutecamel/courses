a = [3, 9]
b = [3, 9]
x = id(a)
print(x)
y = id(b)
print(y)
a[0] = 7
print(a)
print(b)
print(id(a))
print(id(b))
print(type(a))
print("isinstance(a, bytes):", isinstance(a, bytes))
print("isinstance(a, list):", isinstance(a, list))
print("isinstance(a,(bytes,list,str) ):", isinstance(a, (bytes, list, str)))
print("isinstance(a,(bytes,str) ):", isinstance(a, (bytes, str)))
print("dir(a):", dir(a))
try:
    assert isinstance(a, str)
except AssertionError:
    breakpoint()
    print("type error")
print("thankyou")

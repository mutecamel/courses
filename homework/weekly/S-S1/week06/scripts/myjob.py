import mylib  # noqa: F401

y = mylib.func1()
print(y)

try:
    y = mylib.func1(0)
except TypeError as e:
    print(e)

y = mylib.func2()
print(y)

y = mylib.func3(56)
print(y)
y = mylib.func3(x=73)
print(y)
try:
    y = mylib.func3()
except TypeError as e:
    print(e)

y = mylib.func4(22)
print(y)
y = mylib.func4(x=88)
print(y)
y = mylib.func4()
print(y)


print(mylib.area1)
print(mylib.area2)

try:
    print(mylib.func6(a=18, b=179))
except TypeError as e:
    print(e)


print(mylib.func7(18, 179))

print(mylib.func8(18, 179, 82837))
print(mylib.func8(18, 179, 82837, 73628, 2891))
print(mylib.func8(18, 179))

mylib.func9(name="Alice", age=25, city="New York")

tuple_args = (2, 3)
mylib.func10(*tuple_args)
list_args = [5, 7]
mylib.func10(*list_args, named_arg=20)

mylib.func12(72378, 32798, 372)

from mypkg import mylib  # noqa: F401

y = mylib.func1()
print(y)

try:
    y = mylib.func1(0)
except TypeError as e:
    print(e)

y = mylib.func2()
print(y)

y = mylib.func3(45)
print(y)

y = mylib.func3(x=53)
print(y)

y = mylib.func4(48)
print(y)

y = mylib.func4(x=49)
print(y)

y = mylib.func4(x=49)
print(y)

print(mylib.calculate(10, 5, "add"))
print(mylib.calculate(operation="add", b=5, a=10))
print(mylib.calculate(b=5, a=10, operation="subtract"))

try:
    print(mylib.func6(a=10, b=5))
except TypeError as e:
    print(e)

try:
    print(mylib.func7(10, 5, "subtract"))
except TypeError as e:
    print(e)

print(mylib.func8(4, 8, 18, 20))

mylib.func9(name="Alice", age="25", city="New York")

tuple_args = (10, 20)
mylib.func10(*tuple_args)

list_args = (10, 20)
mylib.func10(*list_args)

mylib.func12(7, 8, 9)
breakpoint()

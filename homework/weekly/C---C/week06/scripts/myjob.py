from mypkg import mylib  # noqa: F401

y = mylib.func1()
print(y)

try:
    y = mylib.func1()
except TypeError as e:
    print(e)

y = mylib.func2()
print(y)

y = mylib.func3(45)
print(y)

y = mylib.func3(x=47)
print(y)

try:
    y = mylib.func3()
except TypeError as e:
    print(e)
try:
    mylib.func3(y=47)
except TypeError as e:
    print(e)

y = mylib.func4(48)
print(y)

y = mylib.func4(x=49)
print(y)

y = mylib.func4()
print(y)

print(mylib.calculate(10, 5, "add"))
print(mylib.calculate(operation="add", b=5, a=10))
print(mylib.calculate(5, 8, operation="subtract"))

try:
    print(mylib.func6(a=10, b=5))
except TypeError as e:
    print(e)

try:
    print(mylib.func7(10, 5, "subtract"))
except TypeError as e:
    print(e)

print(mylib.func8())

mylib.func9(name="Alice", age=25, city="New York")

tuple_args = (10, 20)
mylib.func10(*tuple_args)

list_args = [30, 40]
mylib.func10(*list_args)

list_args = [50, 60, "new value"]
mylib.func10(*list_args)

mylib.func12(7, 8, 9)

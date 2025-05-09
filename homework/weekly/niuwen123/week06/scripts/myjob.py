import mylib  # noqa: F401

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

y = mylib.func3(x=47)
print(y)

try:
    y = mylib.func3()
except TypeError as e:
    print(e)

y = mylib.func4(48)
print(y)

y = mylib.func4(x=49)
print(y)

y = mylib.func4()
print(y)

sum_result = mylib.calculate("sum", 2, 4, 6, 8, round_digits=1)
print(f"总和: {sum_result}")
try:
    print(mylib.func6(a=10, b=5))
except TypeError as e:
    print(e)

print(mylib.func7(10, 5, operation="subtract"))

print(mylib.func8(4, 8))

mylib.func9(name="Alice", age=25, city="New York")

tuple_args = (3, 5)
mylib.func10(*tuple_args)

mylib.func12(7, 8, 9)

from mypkg import mylib  # noqa: F401

# 1
y = mylib.func1()
print(y)

try:
    y = mylib.func1(0)
except TypeError as e:
    print(e)

# 2
y = mylib.func2()
print(y)

# 3
y = mylib.func3(25)
print(y)

y = mylib.func3(x=35)
print(y)

try:
    y = mylib.func3()
except TypeError as e:
    print(e)
try:
    y = mylib.func3(y=23)
except TypeError as e:
    print(e)

# 4
y = mylib.func4(45)
print(y)

y = mylib.func4(x=55)
print(y)

y = mylib.func4()
print(y)

# 5
print(mylib.calculate("*", 4, 5))
print(mylib.calculate(operator="*", num1=4, num2=5))
print(mylib.calculate(operator="*", num2=4, num1=5))

# 6
try:
    print(mylib.func6(a=10, b=5))
except TypeError as e:
    print(e)
print(mylib.func6(10, 5))
print(mylib.func6(10, b=5, operator="-"))

# 7
try:
    print(mylib.func7(10, 5, "-"))
except TypeError as e:
    print(e)
print(mylib.func7(10, 5, operator="-"))

# 8
print(mylib.func8(4, 8))
print(mylib.func8(4, 8, 12, 18))

# 9
print(mylib.func9(name="Alice", age=25, city="Beijing"))
print(mylib.func9(name="Bob", hobby="reading", occupation="engineer"))

# 10
tuple_args = (20, 30)
mylib.func10(*tuple_args)
list_args = [40, 50]
mylib.func10(*list_args, named_arg=60)
list_args = [30, 40, "new Value"]
mylib.func10(*list_args)

# 11
mapping = {"named_arg1": 30, "named_arg2": 40}
mylib.func11(5, **mapping)

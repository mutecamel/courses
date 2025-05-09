from mypkg import mylib  # noqa: F401

mylib.func1()
y = mylib.func1()
print(y)
print(type(y))

try:
    a = mylib.func1(0)
except TypeError as e:
    print(e)

y = mylib.func2()
print(y)

y = mylib.func3(2)
print(y)

y = mylib.func3(a=12)
print(y)

try:
    a = mylib.func3()
except TypeError as e:
    print(e)

try:
    mylib.func3(b=12)
except TypeError as e:
    print(e)

b = mylib.func4(12)
print(b)

b = mylib.func4(a=19)
print(b)

print(mylib.calculate_total(10, 5, 0.1))

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

args_list = [30, 40]

# 使用 * 对列表进行解包，并按位置实参传入函数
mylib.func10(*args_list)

args_list = [50, 60, "nem value"]

# 使用 * 对列表进行解包，并按位置实参传入函数
mylib.func10(*args_list)

mylib.func12(7, 8, 9)

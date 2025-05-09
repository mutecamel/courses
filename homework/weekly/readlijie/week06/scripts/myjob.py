from mypkg import mylib  # noqa: F401

y = mylib.func1()  #  106856.0
print(y)  # 返回值是 None什么也没有

try:
    y = mylib.func1(0)
except TypeError as e:
    print(e)

y = mylib.func2()
print(y)

y = mylib.func3(66)  # 位置实参
print(y)

y = mylib.func3(x=5888)  # 命名实参
print(y)

try:
    y = mylib.func3()  # 不传实参
except TypeError as e:
    print(e)

try:
    mylib.func3(y=88)
except TypeError as e:
    print(e)

y = mylib.func4(78)  # 位置
print(y)

y = mylib.func4(x=978)  #  命名
print(y)

y = mylib.func4()  # 默认值
print(y)

print(mylib.calculate(10, 5, "add"))
print(mylib.calculate(b=5, a=10, operation="add"))
print(mylib.calculate(b=5, a=10))
print(mylib.calculate(5, 8, operation="subtract"))

try:
    print(mylib.func6(a=10, b=5, operation="add"))
except TypeError as e:
    print(e)

print(mylib.func7(10, 5, operation="subtract"))

try:
    print(mylib.func7(10, 5, "subtract"))
except TypeError as e:
    print(e)

print(mylib.func8(4, 8, 9))

print(mylib.func8())

mylib.func9(name="alice", age=77, city="harbin")

tuple_args = (101, 222)
mylib.func10(*tuple_args)

list_args = [30, 445]
mylib.func10(*list_args)

list_args = [30, 445, "new york"]
mylib.func10(*list_args)

# 定义一个字典，包含函数所需的命名参数
params = {"a": 1, "b": 2, "c": 3}

# 使用 ** 将字典解包为命名参数
mylib.func11(**params)

mylib.func12(7, 88, 22)

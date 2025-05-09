from mypkg import mylib  # noqa:F401

mylib.func1()


try:
    y = mylib.func1(0)
except TypeError as e:
    print(e)

y = mylib.func2()
print(y)


y = mylib.func3(45)  # 位置实参
print(y)

y = mylib.func3(x=47)  # 位置实参
print(y)

# y = mylib.func3()  # 会报错 用Try捕捉异常
# print(y)
try:
    y = mylib.func3()
except TypeError as e:
    print(e)

try:
    y = mylib.func3(y=47)
except TypeError as e:
    print(e)


y = mylib.func4(48)
print(y)

y = mylib.func4(x=49)
print(y)

y = mylib.func4()  # 不会报错，因为有默认值
print(y)

print(mylib.calculate(10, 5, "add"))  # 要考虑顺序
print(mylib.calculate(operation="add", b=5, a=10))  # 有名字不用考虑顺序
print(mylib.calculate(b=5, a=10))  #
print(mylib.calculate(10, 5, operation="subtract"))  # 要考虑顺序

try:
    print(mylib.func6(a=10, b=5))  # 会报错
except TypeError as e:
    print(e)


print(mylib.func7(10, 5, operation="subtract"))


print(mylib.func8(4, 8, 18, 4))


mylib.func9(name="Alice", age=20, grade="A")


# 创建一个字典
params = {"arg1": 10, "arg2": 20}

# 使用 ** 解包字典并作为命名实参传入函数
result = mylib.func11(**params)
print(result)

# 使用元组作为可迭代对象
tuple_args = (2, 3)
result_with_tuple = mylib.func10(*tuple_args)
print(f"使用元组解包调用函数的结果: {result_with_tuple}")

# 使用列表作为可迭代对象
list_args = [4, 5]
result_with_list = mylib.func10(*list_args)
print(f"使用列表解包调用函数的结果: {result_with_list}")


mylib.func12(7, 8, 9)

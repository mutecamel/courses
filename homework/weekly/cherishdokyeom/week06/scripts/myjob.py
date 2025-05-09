from mypkg import mylib  # type: ignore # noqa: F401

x = mylib.func1()
print(x)

try:
    y = mylib.func1(0)
except TypeError as e:
    print(e)

x = mylib.func2()
print(x)

x = mylib.func3(10)
print(x)

x = mylib.func3(n=10)
print(x)

try:
    x = mylib.func3()
except TypeError as e:
    print(e)

x = mylib.func4(n=40)
print(x)

x = mylib.func4(n=30)
print(x)

x = mylib.func4()
print(x)


print(mylib.cherish(9, 10, "lovely"))
print(mylib.cherish(dokyeom="lovely", a=9, b=10))
print(mylib.cherish(a=9, b=10))

try:
    print(mylib.func6(a=9, b=10))
except TypeError as e:
    print(e)

try:
    print(mylib.func7(9, 10, "lovely"))
except TypeError as e:
    print(e)
print(mylib.func7(9, 10, dokyeom="lovely"))

print(mylib.func8(9, 10, 910))

mylib.func9(name="dokyeom", age=28, city="ser")

# 定义一个元组作为可迭代对象
args_tuple = (1, 2)
result = mylib.func10(*args_tuple)
print(result)

# 定义一个列表作为可迭代对象
args_list = [3, 4]
result = mylib.func10(*args_list)
print(result)

# 定义一个字典作为映射对象
kwargs_dict = {"arg1": 1, "arg2": 2, "arg3": 3}
result = mylib.func11(**kwargs_dict)
print(result)

# 字典可以只包含部分命名参数
kwargs_dict_partial = {"arg1": 5, "arg2": 6}
result = mylib.func11(**kwargs_dict_partial)
print(result)

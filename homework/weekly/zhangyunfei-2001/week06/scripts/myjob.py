import mylib  # noqa: F401

y = mylib.func1()
try:
    y = mylib.func1(0)
except TypeError as e:
    print(e)

y = mylib.func2()
print(y)

y = mylib.func3(100)  ##位置实参
print(y)

y = mylib.func3(x=100)  ##命名实参
print(y)

try:
    y = mylib.func3()
except TypeError as e:
    print(e)  ##输出报错类型

y = mylib.func4()
print(y)
y = mylib.func4(x=49)
print(y)

total = mylib.calculate_total(10, quantity=2, discount=0.1)
print(total)  # 输出 18.0

print(mylib.func6(10, 2, discount=0.1))

print(mylib.func7(10, quantity=2, discount=0.1))

result = mylib.sum_numbers(1, 2, 3, 4, 5)
print(result)

mylib.user_info(name="Alice", age=25, city="New York")


# 定义一个元组
args_tuple = (1, 2)
# 定义一个列表
args_list = [3, 4]

# 使用 * 解包元组并调用函数
result1 = mylib.func10(*args_tuple)
print(result1)

# 使用 * 解包列表并调用函数
result2 = mylib.func10(*args_list, named_arg=20)
print(result2)

params = {"arg1": 1, "arg2": 2, "named_arg": 20}
# 使用 ** 解包字典并调用函数
result = mylib.func11(**params)
print(result)

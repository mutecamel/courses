from mypkg import mylib  # noqa: F401

y = mylib.func1()
print(y)

try:
    y = mylib.func1(0)
except TypeError as e:
    print(e)

y = mylib.func2()
print(y)

y = mylib.func3(60)
print(y)

y = mylib.func3(x=6)
print(y)

try:
    y = mylib.func3()
except TypeError as e:
    print(e)
try:
    mylib.func3(77)
except TypeError as e:
    print(e)

y = mylib.func4(44)
print(y)

y = mylib.func4(x=44)
print(y)

y = mylib.func4()
print(y)

# 使用位置实参调用函数
print("使用位置实参调用函数:")
print(mylib.describe_person("张三", 25, "教师"))

# 使用命名实参调用函数
print("\n使用命名实参调用函数:")
print(mylib.describe_person(name="李四", age=30, job="工程师", 爱好="阅读"))

# 混合使用位置实参和命名实参
print("\n混合使用位置实参和命名实参:")
print(mylib.describe_person("王五", 22, 爱好="篮球", 城市="北京"))

# 正确调用，a、b 用位置传递，c、d 用命名传递
result1 = mylib.func7(1, 2, c=3, d=4)
print(f"a、b 位置传递，c、d 命名传递的结果: {result1}")

# 正确调用，a、b、c、d 都用命名传递
result2 = mylib.func7(a=1, b=2, c=3, d=4)
print(f"a、b、c、d 都用命名传递的结果: {result2}")

# 错误调用示例，会引发 TypeError
try:
    mylib.func7(1, 2, 3, 4)
except TypeError as e:
    print(f"错误调用，引发异常: {e}")


# 调用函数，只传入两个位置实参
result1 = mylib.func8(1, 2)
print(f"只传入两个位置实参的结果: {result1}")

# 调用函数，传入两个位置实参和额外的位置实参
result2 = mylib.func8(1, 2, 3, 4, 5)
print(f"传入两个位置实参和额外位置实参的结果: {result2}")


# 调用函数，只传入两个必需的命名实参
result1 = mylib.func9(name="张三", age=25)
print(result1)

# 调用函数，传入两个必需的命名实参和额外的命名实参
result2 = mylib.func9(name="李四", age=30, 职业="工程师", 爱好="阅读")
print(result2)


# 定义一个元组
data_tuple = (1, 2)
# 使用 * 解包元组作为位置实参传入函数
result1 = mylib.func10(*data_tuple)
print(f"使用元组解包传入位置实参的结果: {result1}")

# 定义一个列表
data_list = [3, 4]
# 使用 * 解包列表作为位置实参传入函数，并指定命名形参 c 的值
result2 = mylib.func10(*data_list, c=5)
print(f"使用列表解包传入位置实参并指定命名形参的结果: {result2}")


# 定义一个字典
person_info = {"name": "王五", "age": 28}

# 使用 ** 解包字典作为命名实参传入函数
result = mylib.func11(**person_info)
print(result)

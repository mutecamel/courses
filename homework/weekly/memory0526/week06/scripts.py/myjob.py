from mypkg import mylib  # noqa: F401

y = mylib.func1()
print(y)  ##因为funct1没有返回值所以y=None

try:
    y = mylib.func1(0)  ##funct1为不含形参的函数所以就没有
except TypeError as e:
    print(e)

y = mylib.func2()
print(y)

y = mylib.func3(25)  ##位置实参
print(y)

y = mylib.func3(x=35)  ##命令实参
print(y)

##有形参的函数不传实参会报错
try:
    y = mylib.func3()
except TypeError as e:
    print(e)

##传没有的形参会报错
try:
    mylib.func3(y=7)
except TypeError as e:
    print(e)

##可以用位置实参上传也可以用命名实参上传
y = mylib.func4(35)
print(y)

y = mylib.func4(x=55)
print(y)

##func4有默认值不传参数也不会报错
y = mylib.func4()
print(y)

print(mylib.func5(1, 2))
print(mylib.func5(1, 2, 3))
print(mylib.func5(1, 2, d=4))
print(mylib.func5(1, b=2, c=3))
print(mylib.func5(a=1, b=2, d=4))


try:
    mylib.func6(a=7, b=2)
except TypeError as e:
    print(e)

try:
    mylib.func7(1, 2, 3)
except TypeError as e:
    print(e)

print(mylib.func8(2, 6, 12))
print(mylib.func9(1, 2, name="Alice", age=30))

# 使用元组解包
args_tuple = (10, 20)
result = mylib.func10(*args_tuple, named="value")
print(result)

# 使用列表解包
args_list = [30, 40]
result = mylib.func10(*args_list, named="another")
print(result)

# 使用字典解包
kwargs_dict = {"named1": "value1", "named2": "value2"}

# 解包字典作为命名参数
result = mylib.func11(10, **kwargs_dict)
print(result)


# 混合使用位置参数和部分解包
partial_dict = {"named2": "partial"}
result = mylib.func11(20, named1="manual", **partial_dict)
print(result)

# 定义函数 func1，没有形参，没有返回值
def func1():
    x = 50
    y = x**0.5 - 7
    print(y)


# 定义函数 func2，没有形参，有返回值
def func2():
    x = 70
    y = x**0.5 - 7
    print(y)
    return y


# 定义函数 func3，只有一个 位置形参 (positional parameter)，先尝试传入 位置实参 (positional argument) 调用，再尝试传入 命名实参 (named argument) 调用，再尝试不传实参 (会报错)
def func3(x):
    y = x**0.5 - 7
    return y


# 定义函数 func4，只有一个 命名形参 (named parameter)，先传入 位置实参 调用，再传入 命名实参 调用，再尝试不传实参 (取默认值)
def func4(x=50):
    y = x**0.5 - 7
    return y


# 定义函数 func5，接受多个位置形参和命名形参，尝试以位置/命名各种不同方式传入实参，注意位置参数必须排在命名参数之前
def calculate(a, b=2, c=3):
    return a + b * c


# 位置实参和命名实参混合使用
result1 = calculate(1, c=4)
print(result1)

result2 = calculate(5, b=6)
print(result2)


# 定义函数 func6，在形参列表中使用 / 来限定只接受位置实参的形参
def func6(a, /, b=2, c=3):
    return a + b * c


# 定义函数 func7，在形参列表中使用 * 来限定只接受命名实参的形参
def func7(a, *, b=2, c=3):
    return a + b * c


# 定义函数 func8，在位置形参的最后，在形参名称前使用 * 允许传入任意数量的位置实参 (被打包为元组)
def func8(*numbers):
    total = 0
    for num in numbers:
        total = total + num
    return total


# 定义函数 func9，在命名形参的最后，在形参名称前使用 ** 允许传入任意数量的命名实参 (被打包为字典)
def func9(**info):
    for key, value in info.items():
        print(f"{key}: {value}")


# 定义函数 func10，接受两个位置形参，一个命名形参，尝试在调用时使用 * 将可迭代对象 (如元组或列表) 自动解包，按位置实参传入
def func10(arg1, arg2, option="default"):
    print(f"第一个参数是: {arg1}")
    print(f"第二个参数是: {arg2}")
    print(f"命名参数（选项）的值是: {option}")


# 定义函数 func12，给函数添加 内嵌文档 (docstring)，给形参和返回值添加 类型注解 (type annotation)，提高函数签名的可读性
def func12(arg1: str, arg2: int, option: str = "default"):
    "多个参数的调用例子"
    print(f"第一个参数是: {arg1}")
    print(f"第二个参数是: {arg2}")
    print(f"命名参数（选项）的值是: {option}")

# 定义函数 func1，没有形参，没有返回值
def func1():
    x = 49
    y = x**0.5 - 7
    print(y)


# 定义函数 func1，没有形参，有返回值
def func2():
    x = 70
    y = x**0.5 - 7
    print(y)
    return y


def func2_2():
    x = 70
    y = x**0.5 - 7
    print(y)
    return y
    # return y + 1  #不会运行


# 定义函数 func3，只有一个 位置形参 (positional parameter)，先尝试传入 位置实参 (positional argument) 调用，再尝试传入 命名实参 (named argument) 调用，再尝试不传实参 (会报错)
def func3(x):  # 位置形参
    y = x**0.5 - 7
    return y


# 定义函数 func4，只有一个 命名形参 (named parameter)，先传入 位置实参 调用，再传入 命名实参 调用，再尝试不传实参 (取默认值)
def func4(x=50):  # 命名形参
    y = x**0.5 - 7
    return y


# 定义函数 func5，接受多个位置形参和命名形参，尝试以位置/命名各种不同方式传入实参，注意位置参数必须排在命名参数之前
def calculate(a, b, operation="add"):
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    else:
        return None


# 定义函数 func6，在形参列表中使用 / 来限定只接受位置实参的形参
def func6(a, /, b, operation="add"):
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    else:
        return None


# 定义函数 func7，在形参列表中使用 * 来限定只接受命名实参的形参
def func7(a, /, b, *, operation="add"):
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    else:
        return None


# 定义函数 func8，在位置形参的最后，在形参名称前使用 * 允许传入任意数量的位置实参 (被打包为元组)
def func8(*numbers):
    total = 0
    for num in numbers:
        total = total + num
    return total


# 定义函数 func9，在命名形参的最后，在形参名称前使用 ** 允许传入任意数量的命名实参 (被打包为字典),不传就是空字典
def func9(**user_info):
    for key, value in user_info.items():
        print(f"{key}: {value}")


# 定义函数 func10，接受两个位置形参，一个命名形参，尝试在调用时使用 * 将可迭代对象 (如元组或列表) 自动解包，按位置实参传入
def func10(arg1, arg2, named_arg=10):
    """
    该函数接收两个位置形参和一个命名形参
    :param arg1: 第一个位置形参
    :param arg2: 第二个位置形参
    :param named_arg: 命名形参，默认值为 10
    :return: 三个参数相加的结果
    """
    return arg1 + arg2 + named_arg


# 定义函数 func11，接受一个命名形参，两个命名形参，尝试在调用时使用 ** 将映射对象 (如字典) 自动解包，按命名实参传入
def func11(arg1, arg2):
    return arg1 + arg2


# 定义函数 func12，给函数添加 内嵌文档 (docstring)，给形参和返回值添加 类型注解 (type annotation)，提高函数签名的可读性
def func12(arg1: str, arg2: int, named_arg: str = "default"):  # 类型的注解
    """
    该函数接收两个位置形参和一个命名形参
    :param arg1: 第一个位置形参
    :param arg2: 第二个位置形参
    :param named_arg: 命名形参，默认值为 10
    :return: 三个参数相加的结果
    """
    return arg1 + arg2 + named_arg

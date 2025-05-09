# 没有形参、没有返回值
def func1():
    x = 49
    y = x**0.5 - 7
    print(y)


# 没有形参、有返回值
def func2():
    x = 70
    y = x**0.5 - 7
    print(y)
    return y


# 有位置形参
def func3(x):
    y = x**0.5 - 7
    return y


# 有命名形参
def func4(x=50):
    y = x**0.5 - 7
    return y


# 多个位置与命名形参
def calculate(operator, num1, num2):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 == 0:
            print("错误：除数不能为零。")
            return None
        return num1 / num2
    else:
        print("错误：不支持的运算符。")
        return None


# 形参中使用“/”
def func6(a, /, b, operator="+"):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        if b == 0:
            print("错误：除数不能为零。")
            return None
        return a / b
    else:
        print("错误：不支持的运算符。")
        return None


# 形参中使用“*”
def func7(a, /, b, *, operator="+"):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        if b == 0:
            print("错误：除数不能为零。")
            return None
        return a / b
    else:
        print("错误：不支持的运算符。")
        return None


# *任意数量位置实参-加法+
def func8(*numbers):
    total = 0
    for num in numbers:
        total = total + num
    return total


# **任意数量命名实参
def func9(**users):
    for key, value in users.items():
        print(f"{key}: {value}")


# *解包可迭代对象
def func10(arg1, arg2, named_arg=10):
    print(f"arg1: {arg1}, arg2: {arg2}, named_arg: {named_arg}")


# 解包映射对象
def func11(positional_arg, named_arg1=10, named_arg2=20):
    """
    该函数接受一个位置形参和两个命名形参
    :param positional_arg: 位置形参
    :param named_arg1: 第一个命名形参，默认值为 10
    :param named_arg2: 第二个命名形参，默认值为 20
    :return: 打印各参数的值
    """
    print(
        f"positional_arg: {positional_arg}, named_arg1: {named_arg1}, named_arg2: {named_arg2}"
    )


#
def func12(arg1: str, arg2: int, named_arg: str = "default") -> None:
    breakpoint()
    """
    多个参数调用的例子,只有print保存

    Parameters
    ----------
    arg1:str
        第一个参数
    arg2:int
        第二个参数

    Returns
    -------
    None
    """
    print(f"位置实参 arg1:{arg1}")
    print(f"位置实参 arg2:{arg2}")
    print(f"命名实参 named_arg:{named_arg}")

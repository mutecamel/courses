def func1():
    x = 50
    y = x**0.5 - 7
    print(y)


def func2():
    x = 70
    y = x**0.5 - 7
    print(y)
    return y


def func3(x):
    y = x**0.5 - 7
    return y


def func4(x=50):
    y = x**0.5 - 7
    return y


def func5(a, b, operation="add"):
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    else:
        return None


def func6(a, /, b, operation="add"):
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    else:
        return None


def func7(a, /, b, *, operation="add"):
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    else:
        return None


def func8(*numbers):
    total = 0
    for num in numbers:
        total = total + num
    return total


def func9(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


def func10(arg1, arg2, named_arg="default"):
    print(f"位置参数 1: {arg1}")
    print(f"位置参数 2: {arg2}")
    print(f"命名参数: {named_arg}")


def func11(arg1, arg2, arg3):
    return arg1 + arg2 + arg3


def func12(a: int, b: int) -> int:
    """
    此函数用于计算两个整数的和。

    参数:
    a (int): 第一个整数。
    b (int): 第二个整数。

    返回:
    int: 两个整数的和。
    """

    return a + b

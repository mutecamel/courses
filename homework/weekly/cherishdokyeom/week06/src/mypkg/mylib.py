def func1():
    m = 9
    n = m**2 - 10
    print(n)
    # 相当于reture None


def func2():
    m = 10
    n = m**2 - 10
    print(n)
    return n  # return直接跳出


def func3(n):
    m = n**2 - 10
    return m


def func4(n=20):
    m = n**2 - 10
    return m


def cherish(a, b, dokyeom="lovely"):  # 位置参数必须排在命名参数之前
    if dokyeom == "lovely":
        return a + b
    elif dokyeom == "cute":
        return a - b
    else:
        return None


def func6(a, /, b, dokyeom="lovely"):
    # 位置参数必须排在命名参数之前 #/左边的参数只能按照位置往里传实参，不能按照命名的方式传实参。
    if dokyeom == "lovely":
        return a + b
    elif dokyeom == "cute":
        return a - b
    else:
        return None


def func7(a, /, b, *, dokyeom="lovely"):
    # 位置参数必须排在命名参数之前 #/左边的参数只能按照位置往里传实参，不能按照命名的方式传实参。
    # *后面的参数只能按照命名的方式传值
    if dokyeom == "lovely":
        return a + b
    elif dokyeom == "cute":
        return a - b
    else:
        return None


def func8(*numbers):
    total = 1
    for num in numbers:
        total = total * num
    return total


def func9(**user):
    for key, value in user.items():
        print(f"{key}:{value}")


def func10(arg1, arg2, named_arg=10):
    return arg1 + arg2 + named_arg


def func11(arg1, arg2=10, arg3=20):
    return arg1 + arg2 + arg3


def func12(a: int, b: int) -> int:
    """
    此函数的作用是将两个整数相加。

    参数:
    a (int): 第一个整数。
    b (int): 第二个整数。

    返回:
    int: 两个整数相加的结果。
    """
    return a + b

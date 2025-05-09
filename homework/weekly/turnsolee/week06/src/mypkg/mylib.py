def func1():  #   没有形参，没有返回值
    x = 20
    y = x**2 - 88 + 88888 / 2
    print(y)


#  相当于 return None


def func2():  #   没有形参，有返回值
    x = 25
    y = x**2 - 88 + 88888 / 2
    print(y)
    return y


def func3(
    x,
):  # 只有一个 位置形参 (positional parameter)，先尝试传入 位置实参 (positional argument) 调用，再尝试传入 命名实参 (named argument) 调用，再尝试不传实参 (会报错)
    y = x**0.5 - 88
    return y


def func4(
    x=88,
):  #  只有一个 命名形参 (named parameter)，先传入 位置实参 调用，再传入 命名实参 调用，再尝试不传实参 (取默认值)
    y = x**0.5 - 88
    return y


def calculate(a, b, operation="add"):
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    else:
        return None

def func8(
    *numbers,
):  #  在位置形参的最后，在形参名称前使用 * 允许传入任意数量的位置实参 (被打包为元组)
    total = 0
    for num in numbers:
        total = total + num
    return total


def func9(
    **user,
):
    for key, value in user.items():
        print(f"{key}:{value}")


#  在命名形参的最后，在形参名称前使用 ** 允许传入任意数量的命名实参 (被打包为字典)


def func10(arg1, arg2, named_arg="default"):
    print(f"位置实参 arg1:{arg1}")
    print(f"位置实参 arg2:{arg2}")
    print(f"位置实参 named_arg:{named_arg}")


# 接受两个位置形参，一个命名形参，尝试在调用时使用 * 将可迭代对象 (如元组或列表) 自动解包，按位置实参传入


def func11(a, b, c):
    """示例函数，接受三个命名参数"""
    print(f"a = {a}, b = {b}, c = {c}")


#  接受一个命名形参，两个命名形参，尝试在调用时使用 ** 将映射对象 (如字典) 自动解包，按命名实参传入


def func12(
    arg1: str, arg2: int, named_arg: str = "default"
) -> None:  # 类型注解 没有约束力
    """
    内嵌文档

    Parameters
    --------
    arg1:str
         第一个参数
    arg2:int
        第二个参数

    Returns
    ---------
    None
    """
    print(f"位置实参 arg1:{arg1}")
    print(f"位置实参 arg2:{arg2}")
    print(f"位置实参 named_arg:{named_arg}")
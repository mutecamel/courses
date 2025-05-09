def func1():
    x = 100
    y = x**0.5 + 3
    print(y)


def func2():
    x = 200
    y = x**0.5 + 3
    print(y)
    return y


def func3(x):
    y = x**0.5 + 3
    return y


def func4(x=8):
    y = x**0.5 + 3
    return y


# 定义一个函数，包含位置形参和命名形参
def describe_person(name, age, job="未指定", **other_info):
    """
    打印人物的信息
    :param name: 位置形参，人物的姓名
    :param age: 位置形参，人物的年龄
    :param job: 命名形参，人物的工作，默认值为 "未指定"
    :param other_info: 命名形参，收集其他任意的关键字参数
    """
    print(f"姓名: {name}")
    print(f"年龄: {age}")
    print(f"工作: {job}")
    for key, value in other_info.items():
        print(f"{key}: {value}")


def func6(a, b, /, c=10, d=20):
    """
    该函数中 a 和 b 只能作为位置实参传入，c 和 d 可作为位置实参或命名实参传入
    :param a: 仅接受位置实参
    :param b: 仅接受位置实参
    :param c: 可接受位置实参或命名实参，默认值为 10
    :param d: 可接受位置实参或命名实参，默认值为 20
    :return: a、b、c、d 四个参数的和
    """
    return a + b + c + d


def func7(a, b, *, c, d):
    """
    此函数中 a 和 b 可以通过位置或命名传递，c 和 d 只能通过命名传递
    :param a: 可以位置或命名传递的参数
    :param b: 可以位置或命名传递的参数
    :param c: 只能命名传递的参数
    :param d: 只能命名传递的参数
    :return: a、b、c、d 四个参数的乘积
    """
    return a * b * c * d


def func8(a, b, *args):
    """
    函数接收两个固定位置形参 a 和 b，以及任意数量的额外位置实参
    :param a: 第一个位置形参
    :param b: 第二个位置形参
    :param args: 接收任意数量的额外位置实参，打包为元组
    :return: 所有参数的总和
    """
    total = a + b
    for num in args:
        total += num
    return total


def func9(name, age, **kwargs):
    """
    该函数接收两个固定的命名形参 name 和 age，以及任意数量的额外命名实参
    :param name: 表示姓名的命名形参
    :param age: 表示年龄的命名形参
    :param kwargs: 接收任意数量的额外命名实参，打包为字典
    :return: 包含所有信息的字符串
    """
    info = f"姓名: {name}，年龄: {age}"
    for key, value in kwargs.items():
        info += f"，{key}: {value}"
    return info


def func10(a, b, c=10):
    return a + b + c


def func11(name, age):
    return f"姓名: {name}，年龄: {age}"


def func12(a: int, b: int) -> int:
    "该函数用于计算两个整数的和"
    return a + b

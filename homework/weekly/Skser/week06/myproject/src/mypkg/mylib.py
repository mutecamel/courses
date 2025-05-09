# mylib.py


def func1():
    """没有形参，没有返回值"""
    print("调用了func1")


def func2():
    """没有形参，有返回值"""
    print("调用了func2")
    return 42


def func3(param):
    """只有一个位置形参"""
    print(f"调用了func3，参数为: {param}")
    return param


def func4(param="默认值"):
    """只有一个命名形参"""
    print(f"调用了func4，参数为: {param}")
    return param


def func5(pos1, pos2, *, named1="默认1", named2="默认2"):
    """多个位置形参和命名形参"""
    print(f"调用了func5，位置参数: {pos1}, {pos2}，命名参数: {named1}, {named2}")
    return pos1, pos2, named1, named2


def func6(pos1, pos2, /):
    """只接受位置实参的形参"""
    print(f"调用了func6，位置参数: {pos1}, {pos2}")
    return pos1, pos2


def func7(*, named1, named2):
    """只接受命名实参的形参"""
    print(f"调用了func7，命名参数: {named1}, {named2}")
    return named1, named2


def func8(*args):
    """任意数量的位置实参"""
    print(f"调用了func8，参数为: {args}")
    return args


def func9(**kwargs):
    """任意数量的命名实参"""
    print(f"调用了func9，参数为: {kwargs}")
    return kwargs


def func10(pos1, pos2, *, named1):
    """两个位置形参，一个命名形参"""
    print(f"调用了func10，位置参数: {pos1}, {pos2}，命名参数: {named1}")
    return pos1, pos2, named1


def func11(*, named1, named2, named3):
    """三个命名形参"""
    print(f"调用了func11，命名参数: {named1}, {named2}, {named3}")
    return named1, named2, named3


def func12(param1: int, param2: str = "默认") -> tuple[int, str]:
    """带有类型注释和文档字符串的函数

    参数:
        param1: 一个整数参数
        param2: 一个字符串参数，有默认值

    返回:
        包含输入参数的元组
    """
    print(f"调用了func12，参数为: {param1}, {param2}")
    return param1, param2

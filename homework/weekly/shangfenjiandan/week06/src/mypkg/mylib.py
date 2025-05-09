def func1():
    x = 50
    y = x**0.5 + 7
    print(y)


def func2():
    x = 60
    y = x**0.5 + 7
    print(y)
    return y


def func3(x):
    y = x**0.5 - 7
    return y


def func4(x=50):
    y = x**0.5 - 7
    return y


def func5(length, width, unit="平方米"):
    area = length * width
    print(f"面积是 {area} {unit}。")
    return area


def func6(length, /, width, unit="平方米"):
    area = length * width
    print(f"面积是 {area} {unit}。")
    return area


def func7(length, /, width, *, unit="平方米"):
    area = length * width
    print(f"面积是 {area} {unit}。")


def func8(*numbers):
    result = 0
    for num in numbers:
        result += num
    return result


def func9(**users):
    for key, value in users.items():
        print(f"{key}: {value}")


def func10(param1, param2, named_param="default"):
    print(f"位置实参 param1: {param1}")
    print(f"位置实参 param1: {param2}")
    print(f"命名实参 named_param: {named_param}")


def func11(name, age):
    print(f"{name} is {age} years old.")


def func12(param1: str, param2: int, named_param: str = "default") -> None:
    """
    多个参数的调用例子,只有print

    Parameters
    ----------
    para1: str
        第一个参数
    para2: int
        第二个参数
    named_param:str
        第三个参数

    Returns
    -------
    None
    """
    print(f"位置实参 param1: {param1}")
    print(f"位置实参 param1: {param2}")
    print(f"命名实参 named_param: {named_param}")

def func1():
    x = 50
    y = x**0.5 - 1
    print(y)


def func2():
    x = 70
    y = x**0.5 - 1
    print(y)
    return y


def func3(x):
    y = x**0.5 - 1
    return y


def func4(x=50):
    y = x**0.5 - 1
    return y


def func5(num):
    if num % 2 != 0:
        raise ValueError("输入必须是偶数")
    return num * 2


def func8(*numbers):
    total = 0
    for num in numbers:
        total = total + num
    return total


def func9(**user_info):
    for key, value in user_info.items():
        print(f"{key}: {value}")


def func10(arg1, arg2, named_arg="default"):
    print(f"位置参数 1: {arg1}")
    print(f"位置参数 2: {arg2}")
    print(f"命名参数: {named_arg}")


def func12(arg1: str, arg2: int, named_arg: str = "default") -> None:
    "多个参数调用例子"
    print(f"位置参数 1: {arg1}")
    print(f"位置参数 2: {arg2}")
    print(f"命名参数: {named_arg}")

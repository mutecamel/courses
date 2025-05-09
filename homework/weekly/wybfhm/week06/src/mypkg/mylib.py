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


def calculate(a, b=1, operation="add"):
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    else:
        return None


def func6(a, /, b=1, operation="add"):
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    else:
        return None


def func7(a, /, b, *, operation="add"):
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    else:
        return None


def func8(*numbers):
    total = 0
    for num in numbers:
        total = total + num
    return total


def func9(**user):
    for key, value in user.items():
        print(f"{key}: {value}")


def func10(positional_arg1, positional_arg2, named_arg="default"):
    print(f"第一个位置形参的值: {positional_arg1}")
    print(f"第二个位置形参的值: {positional_arg2}")
    print(f"命名形参的值: {named_arg}")


def func11(arg1, arg2, arg3="默认值"):
    """
    该函数接受三个命名形参
    :param arg1: 第一个命名形参
    :param arg2: 第二个命名形参
    :param arg3: 第三个命名形参，有默认值
    """
    print(f"第一个命名实参: {arg1}")
    print(f"第二个命名实参: {arg2}")
    print(f"第三个命名实参: {arg3}")


def func12(
    positional_arg1: str, positional_arg2: int, named_arg: str = "default"
) -> None:
    "多个参数的调用例子"
    print(f"第一个位置形参的值: {positional_arg1}")
    print(f"第二个位置形参的值: {positional_arg2}")
    print(f"命名形参的值: {named_arg}")

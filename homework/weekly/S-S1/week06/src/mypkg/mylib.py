def func1():
    x = 50
    y = x**0.8 - 82
    print(y)


def func2():
    x = 100
    y = x**0.8 - 82
    print(y)
    return y


def func3(x):
    y = x**0.8 - 82
    return y


def func4(x=732):
    y = x**0.8 - 82
    return y


# 定义一个函数，包含位置形参和命名形参
def calculate_area(length, width=10):
    return length * width


# 调用函数，使用位置实参和命名实参
area1 = calculate_area(5)  # 使用位置实参传递 length，width 使用默认值
area2 = calculate_area(length=7, width=3)  # 使用命名实参传递参数


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


def func8(*args):
    total = 0
    for num in args:
        total = total + num
    return total


def func9(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


def func10(positional_arg1, positional_arg2, named_arg=10):
    """
    该函数接受两个位置形参和一个带有默认值的命名形参。
    函数会打印出这些参数的值，并返回它们的和。
    """
    print(f"第一个位置形参的值: {positional_arg1}")
    print(f"第二个位置形参的值: {positional_arg2}")
    print(f"命名形参的值: {named_arg}")
    return positional_arg1 + positional_arg2 + named_arg


def func10(positional_arg1, positional_arg2, named_arg=10):
    """
    该函数接受两个位置形参和一个带有默认值的命名形参。
    函数会打印出这些参数的值，并返回它们的和。
    """
    print(f"第一个位置形参的值: {positional_arg1}")
    print(f"第二个位置形参的值: {positional_arg2}")
    print(f"命名形参的值: {named_arg}")
    return positional_arg1 + positional_arg2 + named_arg


tuple_args = (2, 3)
result = func10(*tuple_args)
print(f"三个参数的总和: {result}")


def func12(
    positional_arg1: str, positional_arg2: int, named_arg: str = "default"
) -> None:
    "多个参数的例子"
    print(f"第一个位置形参的值: {positional_arg1}")
    print(f"第二个位置形参的值: {positional_arg2}")
    print(f"命名形参的值: {named_arg}")
    return positional_arg1 + positional_arg2 + named_arg

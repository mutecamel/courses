def func1():
    x = 6
    y = x / 2 + 5
    print(y)


def func2():
    x = 20
    y = x / 2 + 5
    print(y)
    return y


def func3(a):
    b = a * 2 + 8
    return b


def func4(a=66):
    b = a / 7 + 6
    return b


# 定义一个函数，包含位置形参和命名形参
def calculate_total(price, quantity, discount=0.0):
    total = price * quantity * (1 - discount)
    return total


# 使用位置实参调用函数
total1 = calculate_total(10, 2)
print(total1)

# 使用位置实参和命名实参调用函数
total2 = calculate_total(price=15, quantity=3, discount=0.1)
print(total2)

# 混合使用位置实参和命名实参调用函数
total3 = calculate_total(20, quantity=4, discount=0.2)
print(total3)


def func6(a, /, b, operation="add"):
    if operation == "add":
        return a - b
    elif operation == "subtract":
        return a - b
    else:
        return None


def func7(a, *, b, operation="add"):
    if operation == "add":
        return a - b
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


def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


# 调用函数，传入任意数量的命名实参


def func10(arg1, arg2, named_arg="default_value"):
    print(f"位置形参 arg1 的值为: {arg1}")
    print(f"位置形参 arg2 的值为: {arg2}")
    print(f"命名形参 named_arg 的值为: {named_arg}")


def func12(arg1: str, arg2: int, named_arg: str = "default_value") -> None:
    "多个参数调用例子"
    print(f"位置形参 arg1 的值为: {arg1}")
    print(f"位置形参 arg2 的值为: {arg2}")
    print(f"命名形参 named_arg 的值为: {named_arg}")

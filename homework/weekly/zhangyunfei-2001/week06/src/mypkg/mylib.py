def func1():
    x = 100
    y = x**0.5 - 1
    print(y)


def func2():
    x = 10000
    y = x**0.5 - 1
    print(y)
    return y


def func3(x):
    y = x**0.5 - 2
    return y


def func4(x=100):
    y = x**0.5 - 2
    return y


# 定义一个函数，包含位置形参和命名形参
def calculate_total(price, quantity, discount=0):
    return price * quantity * (1 - discount)


def func6(price, /, quantity, discount=0):  ##/左边只能按位置传实参
    return price * quantity * (1 - discount)


def func7(price, *, quantity, discount=0):  ##*右边只能按位置传实参
    return price * quantity * (1 - discount)


def sum_numbers(*numbers):
    total = 0
    for num in numbers:
        total = total + num
    return total


def user_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")


user_info(name="Alice", age=25, city="New York")


def func10(arg1, arg2, named_arg=10):
    "自动解包"
    return arg1 + arg2 + named_arg


def func11(arg1, arg2, named_arg=10):
    return arg1 + arg2 + named_arg

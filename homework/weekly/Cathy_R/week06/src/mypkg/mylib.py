def func1():
    x = 50
    y = x**0.5 - 7
    print(y)


def func2():
    x = 70
    y = x**0.5 - 7
    print(y)
    return y


def func2_2():
    x = 70
    y = x**0.5 - 7
    print(y)
    return y
    return y + 1


def func3(x):
    y = x**0.5 - 7
    return y


def func4(x=50):
    y = x**0.5 - 7
    return y


def calculate_total(price, quantity, discount=0):
    total = price * quantity * (1 - discount)
    print(f"The total cost is {total}.")


# 使用位置实参调用
calculate_total(10, 2)
# 使用位置实参和命名实参混合调用
calculate_total(10, 2, discount=0.1)
# 全部使用命名实参调用
calculate_total(price=15, quantity=3, discount=0.2)


def func6(price, /, quantity, discount=0):
    total = price * quantity * (1 - discount)
    print(f"The total cost is {total}.")


def func7(price, /, quantity, *, discount=0):
    total = price * quantity * (1 - discount)
    print(f"The total cost is {total}.")


def func8(*args):
    total = 0
    for num in args:
        total = total + num
    return total


result = func8(1, 2, 3, 4, 5)
print(result)


def func9(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


func9(name="Alice", age=25, city="New York")


def func10(arg1, arg2, named_arg=10):
    return arg1 + arg2 + named_arg


# 定义可迭代对象（这里使用元组）
positional_args = (3, 5)

# 使用 * 解包可迭代对象并传入函数
result = func10(*positional_args)
print(result)

# 也可以使用列表
positional_args_list = [2, 4]
result_list = func10(*positional_args_list)
print(result_list)


def func12(a: int, b: int) -> int:
    """
    此函数用于计算两个整数的和。

    参数:
    a (int): 第一个用于相加的整数。
    b (int): 第二个用于相加的整数。

    返回:
    int: 两个整数相加的结果。
    """
    return a + b

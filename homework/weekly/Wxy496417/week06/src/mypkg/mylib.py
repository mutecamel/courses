def func1():
    x = 49
    y = x**0.5 - 7
    print(y)


def func2():
    x = 120
    y = x**0.5 - 7
    print(y)
    return y


def func3(x):
    y = x**0.5 - 7
    return y


def func4(x=55):
    y = x**0.5 - 7
    return y


# 定义函数，其中 base_score 和 bonus 是位置形参，special_reward 是命名形参
def calculate_score(base_score, bonus, special_reward=False):
    total_score = base_score + bonus
    if special_reward:
        total_score += 10
    return total_score


def func6(base_score, /, bonus, special_reward=False):
    total_score = base_score + bonus
    if special_reward:
        total_score += 10
    return total_score


def func7(base_score, /, bonus, *, special_reward=False):
    total_score = base_score + bonus
    if special_reward:
        total_score += 10
    return total_score


def func8(*numbers):
    """计算任意数量数字的总和"""
    total = 0
    for num in numbers:
        total += num
    return total


def func9(**info):
    """打印关于一个人的信息"""
    for key, value in info.items():
        print(f"{key}: {value}")


def func10(arg1, arg2, named_arg=10):
    return arg1 + arg2 + named_arg


# 定义 func11 函数，接受三个命名形参
def func11(param1=1, param2=2, param3=3):
    return param1 + param2 + param3


def func12(arg1: int, arg2: int, named_arg: int = 10) -> None:
    "多个参数调用的例子"
    return arg1 + arg2 + named_arg

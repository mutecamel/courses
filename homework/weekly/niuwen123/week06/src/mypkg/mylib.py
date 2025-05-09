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


def calculate(stat_type, *numbers, weight=None, round_digits=2):
    """
    进行不同类型统计计算的函数
    :param stat_type: 统计类型，如 'mean', 'weighted_mean', 'sum'
    :param numbers: 输入的数值
    :param weight: 计算加权平均值时的权重列表，默认值为 None
    :param round_digits: 结果保留的小数位数，默认值为 2
    :return: 计算结果
    """
    if stat_type == "mean":
        if not numbers:
            return 0
        return round(sum(numbers) / len(numbers), round_digits)
    elif stat_type == "weighted_mean":
        if not numbers:
            return 0
        if weight is None:
            weight = [1] * len(numbers)
        if len(weight) != len(numbers):
            raise ValueError("权重列表的长度必须和数值列表的长度一致")
        weighted_sum = sum(num * w for num, w in zip(numbers, weight))
        total_weight = sum(weight)
        return round(weighted_sum / total_weight, round_digits)
    elif stat_type == "sum":
        return round(sum(numbers), round_digits)
    else:
        raise ValueError("不支持的统计类型，请使用 'mean', 'weighted_mean', 'sum'")


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


def func8(*numbers):
    total = 0
    for num in numbers:
        total = total + num
    return total


def func9(**user):
    for key, value in user.items():
        print(f"{key}: {value}")


def func10(arg1, arg2, named_arg="default"):
    print(f"位置实参 arg1: {arg1}")
    print(f"位置实参 arg2: {arg2}")
    print(f"命名实参 named_arg: {named_arg}")


def func12(arg1: str, arg2: int, named_arg: str = "default") -> None:
    "哈哈哈"
    print(f"位置实参 arg1: {arg1}")
    print(f"位置实参 arg2: {arg2}")
    print(f"命名实参 named_arg: {named_arg}")

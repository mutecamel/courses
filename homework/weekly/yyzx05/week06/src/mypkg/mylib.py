def func1():
    x = 50
    y = x**0.5 - 7
    print(y)


def func2():
    x = 80
    y = x**0.5 - 7
    print(y)
    return y


def func2_2():
    x = 80
    y = x**0.5 - 7
    print(y)
    return y


def func3(x):
    y = x**0.5 - 7
    return y


def func4(x=69):
    y = x**0.5 - 7
    return y


def func5(price, quantity, discount=0):
    return price * quantity * (1 - discount)


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


def func10(arg1, arg2, named_arg=0):
    result = arg1 + arg2 + named_arg
    return result


def func11(param1, param2, param3):
    return f"param1 的值是 {param1}，param2 的值是 {param2}，param3 的值是 {param3}"


def func12(arg1: str, arg2: int, named_arg: str = "0") -> None:
    "多个参数的调用例子"
    result = arg1 + arg2 + named_arg
    return result

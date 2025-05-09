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


def calculate(a, b, operation="add"):
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    else:
        return None


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
    print(f"位置实参arg1: {arg1}")
    print(f"位置实参arg2: {arg2}")
    print(f"命名实参named_arg: {named_arg}")


def func11(arg1, arg2, named_arg="default"):
    print(f"位置实参 arg1: {arg1}")
    print(f"位置实参 arg2: {arg2}")
    print(f"命名实参 named_arg: {named_arg}")


def func12(arg1: str, arg2: int, named_arg="default") -> None:
    "多个参数的调用例子"
    print(f"位置实参arg1: {arg1}")
    print(f"位置实参arg2: {arg2}")
    print(f"命名实参named_arg: {named_arg}")

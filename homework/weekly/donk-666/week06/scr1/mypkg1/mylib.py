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


def func4(x=100):
    y = x**0.5 - 8
    return y


def func5(*args, **kwargs):
    print("位置参数:", args)
    print("命名参数:", kwargs)


# 仅传入位置参数
func5(1, 2, 3)

# 仅传入命名参数
func5(a=10, b=20)

# 同时传入位置参数和命名参数
func5(1, 2, a=10, b=20)


def func6(a, /, b, operation="add"):
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


def func9(**users):
    for key, value in users.items():
        print(f"{key}:{value}")

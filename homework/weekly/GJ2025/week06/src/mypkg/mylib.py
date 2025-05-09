def func1():
    x = 49
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


def calculate_total(price, quantity, tax_rate=0.1, discount=0):
    subtotal = price * quantity
    total_tax = subtotal * tax_rate
    total_discount = subtotal * discount
    total = subtotal + total_tax - total_discount
    return total


def func6(price, quantity, /, tax_rate=0.1, discount=0):
    subtotal = price * quantity
    total_tax = subtotal * tax_rate
    total_discount = subtotal * discount
    total = subtotal + total_tax - total_discount
    return total


def func7(price, quantity, tax_rate=0.1, *, discount=0):
    subtotal = price * quantity
    total_tax = subtotal * tax_rate
    total_discount = subtotal * discount
    total = subtotal + total_tax - total_discount
    return total


def func8(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total


def func9(**user):
    for key, value in user.items():
        print(f"{key}: {value}")


def func10(pos1, pos2, named_param=10):
    print(f"位置实参 pos1: {pos1}")
    print(f"位置实参 pos2: {pos2}")
    print(f"命名实参 named_param: {named_param}")


def func11(positional_arg, named_arg1=10, named_arg2=20):
    print(f"位置形参: {positional_arg}")
    print(f"命名形参 1: {named_arg1}")
    print(f"命名形参 2: {named_arg2}")


def func12(pos1: str, pos2: int, named_param: str = 10) -> None:
    """
    多个参数的调用例子,只有print

    Parameters
    ----------
    pos1: str
        第一个参数
    pos2: int
        第二个参数

    Returns
    -------
    None
    """
    print(f"位置实参 pos1: {pos1}")
    print(f"位置实参 pos2: {pos2}")
    print(f"命名实参 named_param: {named_param}")

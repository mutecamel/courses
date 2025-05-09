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
    return y + 1


def func3(x):
    y = x**0.5 - 7
    return y


def func4(x=55):
    y = x**0.5 - 7
    return y


def calculate_total_price(quantity, price_per_item, discount=0, shipping_fee=5):
    """
    计算商品的总价，考虑折扣和运费
    :param quantity: 商品数量，位置形参
    :param price_per_item: 每件商品的价格，位置形参
    :param discount: 折扣比例，命名形参，默认值为 0
    :param shipping_fee: 运费，命名形参，默认值为 5
    :return: 商品总价
    """
    subtotal = quantity * price_per_item
    discounted_price = subtotal * (1 - discount)
    total_price = discounted_price + shipping_fee
    return total_price


# 定义函数 func6，使用 / 限定只接受位置实参的形参
def func6(a, b, /):
    return a + b


# 定义函数 func7，使用 * 限定只接受命名实参的形参
def func7(*, c, d):
    return c * d


# 定义函数 func8，使用 * 允许传入任意数量的位置实参（被打包为元组）
def func8(x, y, *args):
    result = x + y
    for num in args:
        result += num
    return result


# 定义函数 func9，使用 ** 允许传入任意数量的命名实参（被打包为字典）
def func9(m, n, **kwargs):
    result = m - n
    for value in kwargs.values():
        result += value
    return result


# 定义函数 func10，接受两个位置形参，一个命名形参
def func10(p, q, r=0):
    return p * q + r


# 定义函数 func11，接受三个命名形参
def func11(s, t, u=0):
    return s + t + u


def func12(arg1: str, arg2: int, named_arg: str = "default") -> None:
    print(f"位置实参 arg1:{arg1}")
    print(f"位置实参 arg2:{arg2}")
    print(f"位置实参 named_arg:{named_arg}")

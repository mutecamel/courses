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


def process_order(product_name, unit_price, quantity=1, discount=0.0, tax_rate=0.1):
    """
    处理订单并计算最终总价

    :param product_name: 商品名称，位置形参
    :param unit_price: 商品单价，位置形参
    :param quantity: 购买数量，命名形参，默认值为 1
    :param discount: 折扣比例，命名形参，默认值为 0.0
    :param tax_rate: 税率，命名形参，默认值为 0.1
    :return: 最终订单总价
    """
    subtotal = unit_price * quantity
    discounted_subtotal = subtotal * (1 - discount)
    tax_amount = discounted_subtotal * tax_rate
    total = discounted_subtotal + tax_amount
    print(
        f"你购买的商品是 {product_name}，单价为 {unit_price} 元，购买了 {quantity} 件。"
    )
    print(f"享受了 {discount * 100}% 的折扣，需缴纳 {tax_rate * 100}% 的税。")
    print(f"最终订单总价是 {total} 元。")
    return total


# 混合使用位置实参和命名实参调用函数
order_total = process_order("智能手机", 5000, quantity=2, discount=0.1)


def func6(product_name, /, unit_price, quantity=1, discount=0.0, tax_rate=0.1):
    """
    处理订单并计算最终总价

    :param product_name: 商品名称，位置形参
    :param unit_price: 商品单价，位置形参
    :param quantity: 购买数量，命名形参，默认值为 1
    :param discount: 折扣比例，命名形参，默认值为 0.0
    :param tax_rate: 税率，命名形参，默认值为 0.1
    :return: 最终订单总价
    """
    try:
        # 将 unit_price 转换为浮点数
        unit_price = float(unit_price)
        subtotal = unit_price * quantity
        discounted_subtotal = subtotal * (1 - discount)
        tax_amount = discounted_subtotal * tax_rate
        total = discounted_subtotal + tax_amount
        print(
            f"你购买的商品是 {product_name}，单价为 {unit_price} 元，购买了 {quantity} 件。"
        )
        print(f"享受了 {discount * 100}% 的折扣，需缴纳 {tax_rate * 100}% 的税。")
        print(f"最终订单总价是 {total} 元。")
        return total
    except ValueError:
        print("输入的单价不是有效的数字，请检查输入。")
        return None


def func7(product_name, /, unit_price, *, quantity=1, discount=0.0, tax_rate=0.1):
    """
    处理订单并计算最终总价

    :param product_name: 商品名称，位置形参
    :param unit_price: 商品单价，位置形参
    :param quantity: 购买数量，命名形参，默认值为 1
    :param discount: 折扣比例，命名形参，默认值为 0.0
    :param tax_rate: 税率，命名形参，默认值为 0.1
    :return: 最终订单总价
    """
    try:
        # 将 unit_price 转换为浮点数
        unit_price = float(unit_price)
        subtotal = unit_price * quantity
        discounted_subtotal = subtotal * (1 - discount)
        tax_amount = discounted_subtotal * tax_rate
        total = discounted_subtotal + tax_amount
        print(
            f"你购买的商品是 {product_name}，单价为 {unit_price} 元，购买了 {quantity} 件。"
        )
        print(f"享受了 {discount * 100}% 的折扣，需缴纳 {tax_rate * 100}% 的税。")
        print(f"最终订单总价是 {total} 元。")
        return total
    except ValueError:
        print("输入的单价不是有效的数字，请检查输入。")
        return None


def func8(*numbers):
    """
    计算传入的所有数字的总和
    :param numbers: 任意数量的位置实参，代表要相加的数字
    :return: 这些数字的总和
    """
    total = 0
    for num in numbers:
        total = total + num
    return total


def func9(name, age, **extra_info):
    user = {"name": name, "age": age}
    user.update(extra_info)
    for key, value in user.items():
        print(f"{key}: {value}")


def func10(arg1, arg2, named_arg=10):
    """
    此函数接受两个位置形参和一个命名形参
    :param arg1: 第一个位置形参
    :param arg2: 第二个位置形参
    :param named_arg: 命名形参，默认值为 10
    :return: 打印传入参数的信息
    """
    print(f"位置实参 arg1 的值为: {arg1}")
    print(f"位置实参 arg2 的值为: {arg2}")
    print(f"命名实参 named_arg 的值为: {named_arg}")


def func11(param1=0, param2=1, param3=2):
    """
    此函数接受三个命名形参
    :param param1: 第一个命名形参，默认值为 0
    :param param2: 第二个命名形参，默认值为 1
    :param param3: 第三个命名形参，默认值为 2
    :return: 打印传入参数的信息
    """
    print(f"命名实参 param1 的值为: {param1}")
    print(f"命名实参 param2 的值为: {param2}")
    print(f"命名实参 param3 的值为: {param3}")


def func12(arg1: str, arg2: int, named_arg: str = 10):
    """
    此函数接受两个位置形参和一个命名形参
    :param arg1: 第一个位置形参
    :param arg2: 第二个位置形参
    :param named_arg: 命名形参，默认值为 10
    :return: 打印传入参数的信息
    """
    print(f"位置实参 arg1 的值为: {arg1}")
    print(f"位置实参 arg2 的值为: {arg2}")
    print(f"命名实参 named_arg 的值为: {named_arg}")


def configure_settings(default_settings, **custom_settings):
    """
    整合默认设置和自定义设置
    :param default_settings: 字典类型，默认设置
    :param custom_settings: 任意数量的命名实参，自定义设置
    :return: 整合后的设置字典
    """
    settings = default_settings.copy()
    settings.update(custom_settings)
    for key, value in settings.items():
        print(f"{key}: {value}")
    return settings


default = {"font_size": 12, "background_color": "white"}
configure_settings(default, font_size=14, text_color="black")

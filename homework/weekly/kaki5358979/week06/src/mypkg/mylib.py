def func1():  # 没有形参，没有返回值
    x = 50
    y = x**0.5 - 7
    print(y)  # 将内容输出到控制台，仅供查看，不影响程序逻辑


def func2():  # 没有形参，有返回值
    x = 81
    y = x**0.5 - 7
    print(y)
    return y  # 结束函数的执行，并将值返回给调用者，这个值可以被其他代码使用


def func3(x):  # 有一个位置形参 (positional parameter)
    y = x**0.5 - 7
    return y


def func4(x=49):  # 有一个命名形参 (named parameter)
    y = x**0.5 - 7
    return y


# 接受多个位置形参和命名形参，注意位置参数必须排在命名参数之前:
def func5(a, b, operation="add"):
    if operation == "add":
        return a + b
    elif operation == "substract":
        return a - b
    else:
        return None


# / 限定其左侧的形参只接受位置实参
def func6(a, /, b, operation="add"):
    if operation == "add":
        return a + b
    elif operation == "substract":
        return a - b
    else:
        return None


# * 限定其右侧的形参只接受命名实参
def func7(a, b, *, operation="add"):
    if operation == "add":
        return a + b
    elif operation == "substract":
        return a - b
    else:
        return None


# 在形参名称前使用 * 允许传入任意数量的位置实参(打包成元组)
def func8(*numbers):
    total = 0
    for num in numbers:
        total = total + num
    return total


# 形参名称前使用 ** 允许传入任意数量的命名实参 (打包为字典)
def func9(**user):
    for key, value in user.items():
        print(f"{key}:{value}")


# 在调用时使用 * 将可迭代对象 (如元组或列表) 自动解包，按位置实参传入
def func10(a, b, name="Unknown"):
    print(f"a = {a}, b = {b}, name = {name}")


# 在调用时使用 ** 将映射对象 (如字典) 自动解包，按命名实参传入
def func11(x, name="Unknown", age=0):
    print(f"x = {x}, name = {name}, age = {age}")


# 给函数添加 内嵌文档 (docstring)，给形参和返回值添加 类型注解 (type annotation)，提高函数签名的可读性
def func12(name: str, age: int = 18, is_student: bool = True) -> str:
    """
    根据用户信息生成欢迎消息。
    Examples:
        >>> func12("Alice", 20, False)
        'Hello Alice, age 20, student: False'
    """
    return f"Hello {name}, age {age}, student: {is_student}"

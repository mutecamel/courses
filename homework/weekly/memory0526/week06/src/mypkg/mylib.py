def func1():  ##func1没有形参也没有返回值
    x = 25
    y = x**0.5 - 7
    print(y)


def func2():  ##func2没有形参,有返回值
    x = 36
    y = x**0.5 - 7
    print(y)
    return y


def func3(x):  ##fun3有一个位置形参,给x赋值的时候是实参
    y = x**0.5 - 7
    return y


def func4(x=24):  ##fun3有一个命名形参
    y = x**0.5 - 7
    return y


##函数中有多个位置形参和命名形参，未知参数必须要在命名参数之后，位置实参必须要按照位置输入参数，命令实参则可以打乱顺序
def func5(a, b, c=0, d=0):
    return f"a={a}, b={b}, c={c}, d={d}"


##在形参列表中使用 / 来限定只接受位置实参的形参
def func6(a, /, b, c=0, d=0):
    return f"a={a}, b={b}, c={c}, d={d}"


##再形参列表中使用 * 来限定只接受命名实参的形参
def func7(a, b, *, c=0, d=0):
    return f"a={a}, b={b}, c={c}, d={d}"


##定义函数 func8，在位置形参的最后，在形参名称前使用 * 允许传入任意数量的位置实参 (被打包为元组)
def func8(*numbers):
    total = 0
    for num in numbers:
        total = total + num
    return total


##定义函数 func9，在命名形参的最后，在形参名称前使用 ** 允许传入任意数量的命名实参 (被打包为字典)
def func9(a, b, **kwargs):
    # 将位置参数和关键字参数组合成一个字典
    result = {"a": a, "b": b, "additional_args": kwargs}
    return result


##定义函数 func10，接受两个位置形参，一个命名形参，尝试在调用时使用 * 将可迭代对象 (如元组或列表) 自动解包，按位置实参传入
def func10(pos1, pos2, named=None):
    """
    接受两个位置形参和一个命名形参的函数
    """
    return {"positional_1": pos1, "positional_2": pos2, "named_argument": named}


##定义函数 func11，接受一个位置形参，两个命名形参，尝试在调用时使用 ** 将映射对象 (如字典) 自动解包，按命名实参传入
def func11(pos, named1=None, named2=None):
    return {"positional": pos, "named_arg1": named1, "named_arg2": named2}


##使用注解,但对结果没有约束力
def func12(pos: int, named1=None, named2=None):
    """
    接受一个位置形参和两个命名形参的函数
    """
    return {"positional": pos, "named_arg1": named1, "named_arg2": named2}

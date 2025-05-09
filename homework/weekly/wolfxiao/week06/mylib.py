# func1：无参无返回值
def func1():
    print("func1 执行，无参无返回")

# func2：无参有返回值
def func2():
    return "这是 func2 的返回值"

# func3：一个位置形参
def func3(a):
    print(f"func3 接收位置参数 a: {a}")

# func4：一个命名形参（带默认值）
def func4(a=10):
    print(f"func4 接收参数 a: {a}")

# func5：多个位置形参和命名形参
def func5(a, b, c=3):
    print(f"func5 位置参数 a: {a}, b: {b}, 命名参数 c: {c}")

# func6：用 / 限定只接受位置实参的形参
def func6(a, /, b):
    print(f"func6 位置参数 a: {a}, b: {b}")

# func7：用 * 限定只接受命名实参的形参
def func7(*, a):
    print(f"func7 命名参数 a: {a}")

# func8：接受任意数量位置实参（打包为元组）
def func8(*args):
    print(f"func8 接收任意位置参数: {args}")

# func9：接受任意数量命名实参（打包为字典）
def func9(**kwargs):
    print(f"func9 接收任意命名参数: {kwargs}")

# func10：接受两个位置形参，一个命名形参，测试解包
def func10(a, b, c=3):
    print(f"func10 位置参数 a: {a}, b: {b}, 命名参数 c: {c}")

# func11：接受一个位置形参，两个命名形参，测试解包
def func11(a, b=2, c=3):
    print(f"func11 位置参数 a: {a}, 命名参数 b: {b}, c: {c}")

# func12：带 docstring 和类型注解
def func12(a: int, b: int) -> int:
    """
    计算两个整数的和。

    :param a: 第一个整数
    :param b: 第二个整数
    :return: 两个整数的和
    """
    return a + b
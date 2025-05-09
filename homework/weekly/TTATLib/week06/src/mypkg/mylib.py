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

# 定义一个函数，包含位置形参和命名形参
def calculate_area(length, width=10):
    """
    计算矩形的面积
    :param length: 矩形的长，位置形参
    :param width: 矩形的宽，命名形参，默认值为 10
    :return: 矩形的面积
    """
    return length * width

# 使用位置实参调用函数
area1 = calculate_area(5)
print(f"使用位置实参，面积为: {area1}")

# 使用位置实参和命名实参混合调用函数
area2 = calculate_area(8, width=12)
print(f"使用位置实参和命名实参混合，面积为: {area2}")

# 只使用命名实参调用函数
area3 = calculate_area(length=6, width=15)
print(f"只使用命名实参，面积为: {area3}")

def func6(length, /,  width=10):
    """
    计算矩形的面积
    :param length: 矩形的长，位置形参
    :param width: 矩形的宽，命名形参，默认值为 10
    :return: 矩形的面积
    """
    return length * width

# 使用位置实参调用函数
area1 = calculate_area(5)
print(f"使用位置实参，面积为: {area1}")

# 使用位置实参和命名实参混合调用函数
area2 = calculate_area(8, width=12)
print(f"使用位置实参和命名实参混合，面积为: {area2}")



def func8(*numbers):
    total = 0
    for num in numbers:
        total = total + num
    return total

def func9(**user_info):
    return user_info
user = func9(name="Alice", age=25, city="New York")
print(user)



def func10(a, b, c=10):
    print(f"位置形参 a = {a}, 位置形参 b = {b}, 命名形参 c = {c}")

# 元组解包
data_tuple = (20, 30)
func10(*data_tuple)  # 输出：a=20, b=30, c=10（c 使用默认值）

# 列表解包 + 显式命名形参
data_list = [5, 15]
func10(*data_list, c=25)  # 输出：a=5, b=15, c=25（c 被显式赋值）


# 定义 func11 函数，接受三个命名形参
def func11(param1=0, param2=1, param3=2):
    print(f"param1 的值是: {param1}")
    print(f"param2 的值是: {param2}")
    print(f"param3 的值是: {param3}")
# 创建一个字典作为映射对象
data_dict = {
    "param1": 10,
    "param2": 20,
    "param3": 30
}
# 使用 ** 解包字典并将其作为命名实参传入函数
func11(**data_dict)



def func12(a: int, b: int, multiplier: float = 1.0) -> float:
    """
    计算两个整数的和与倍数因子的乘积。
    
    参数:
        a (int): 参与运算的第一个整数。
        b (int): 参与运算的第二个整数。
        multiplier (float, 可选): 倍数因子，默认值为 1.0。用于放大 `(a + b)` 的结果。
    
    返回:
        float: `(a + b) * multiplier` 的计算结果，返回值为浮点数。
    """
    return (a + b) * multiplier


    

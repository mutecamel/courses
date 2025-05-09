import random  # 0-1随机数

x = 1.235  #  浮点数
print(type(x))  #   <class 'float'>

y = float("1.235")
print(type(y))  #   <class 'float'>

assert x == y

x = 511 / 3
print(
    x, type(x)
)  #   170.33333333333334 <class 'float'>  不要做等号判断 浮点数有四舍五入误差

x = random.random()
print(x)  # 函数返回值是float浮点数

assert not 0.0
assert 0.1

nan = float("nan")  # 浮点数特殊值，缺失值  跟任何数计算都是nan
print(nan + 222)  # nan
print(nan < 27986)  # false
print(nan > 27986)  # false
print(nan == 27986)  # false

pinf = float("inf")  # 正无穷
print(3.14e5)  #   314000.0
print(3.14e-4)  #   0.000314
print(pinf > 1e200)  #  true
print(pinf > pinf)  # false
print(pinf == pinf)

ninf = float("-inf")
print(ninf)  # 负无穷

assert pinf > ninf

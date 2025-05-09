import random

x = 3.14
print(type(x))

y = float("3.14")

print(type(y))

assert x == y
x = 5 / 3
print(x, type(x))


x = random.random()  # 得到随机数
print


# 什么当作false
# assert  0.0#会报错,不要对浮点数做等号的判断
assert not 0.0
# 特殊浮点数
nan = float("nan")  # 能够通过，特殊值，当作缺失值
print(nan + 3)  # 缺失值和其他数运算都是缺失的
print(nan < 3)
print(nan > 3)
print(nan == 3)
# 正无穷
pinf = float("inf")
print(3.14e2)
print(pinf > 1e200)
print(pinf > pinf)  # 正无穷不比自己大
# 负无穷
ninf = float("-inf")
print(ninf)

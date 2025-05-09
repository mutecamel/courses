import random

# 定义浮点数并检查类型
x = 2.718
print(type(x))

# 通过字符串转换为浮点数并检查类型
y = float('2.718')
print(type(y))

# 断言两个浮点数相等
assert x == y

# 浮点数运算
x = 5.0
y = 2.0
print(x - y, type(x - y))

# 生成随机浮点数
x = random.random()
print(x)

# 检查浮点数是否为0
assert not 0.0

# 处理特殊浮点数NaN（非数字）
nan = float('nan')
print(nan + 5)
print(nan > 5)
print(nan < 5)
print(nan == 5)

# 处理正无穷大
pinf = float('inf')
print(pinf - 1020)
print(pinf > 1020)
print(pinf == pinf)

# 处理负无穷大
ninf = float('-inf')
print(ninf + 10)
print(ninf < -10)
print(ninf == ninf)

breakpoint()

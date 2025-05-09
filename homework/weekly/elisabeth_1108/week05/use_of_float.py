# 定义一个浮点数
float_number = 3.14
print(float_number)

# 浮点数有误差
a = 0.1
b = 0.2
print(a + b)

# 要比较浮点数，要设定范围
a = 0.1 + 0.2
b = 0.3
epsilon = 1e-9
if abs(a - b) < epsilon:
    print("a and b are considered equal.")
else:
    print("a and b are not equal.")

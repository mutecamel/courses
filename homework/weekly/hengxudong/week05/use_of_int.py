i = 42
x = 26
y = 7
z = x + y
print(z)

x = 5
y = 17
print(y // x)  # 整除
print(y / x)
print(y % x)  # 余数

assert 5

try:
    assert 0
except AssertionError as e:
    print(e)

x = 9927941346

# 整数不能被迭代，不能被提取


# 十进制转二进制
decimal_num = 10
binary_num = bin(decimal_num)
print(binary_num)  # 输出：0b1010

# 十进制转八进制
octal_num = oct(decimal_num)
print(octal_num)  # 输出：0o12

# 十进制转十六进制
hexadecimal_num = hex(decimal_num)
print(hexadecimal_num)  # 输出：0xa

# 二进制、八进制、十六进制转十进制
bin_to_dec = int("1010", 2)
oct_to_dec = int("12", 8)
hex_to_dec = int("a", 16)
print(bin_to_dec, oct_to_dec, hex_to_dec)  # 输出：10 10 10

import math

num = 9
# 开平方
square_root = math.sqrt(num)
print(square_root)  # 输出：3.0

# 求绝对值
abs_num = abs(-5)
print(abs_num)  # 输出：5

# 向上取整
ceil_num = math.ceil(3.14)
print(ceil_num)  # 输出：4

# 向下取整
floor_num = math.floor(3.99)
print(floor_num)  # 输出：3

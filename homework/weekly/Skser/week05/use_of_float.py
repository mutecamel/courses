# 浮点数 (float)
float_example = 3.14159

# 使用内置函数检视对象
print(f"ID: {id(float_example)}")
print(f"Type: {type(float_example)}")
print(f"Is instance of float: {isinstance(float_example, float)}")
print(f"Attributes and methods: {dir(float_example)}")
print(f"Float representation: {str(float_example)}")

# 数学运算符支持
result = float_example + 1.0
print(f"Addition: {result}")

# 判断相等
assert abs(float_example - 3.14159) < 1e-9, "Floats are not equal"

# 比较运算符支持
another_float = 3.14160
if another_float > float_example:
    print("another_float is greater than float_example")

# 布尔值判断
zero_float = 0.0
non_zero_float = 3.14159
print(f"Zero float evaluates to: {bool(zero_float)}")
print(f"Non-zero float evaluates to: {bool(non_zero_float)}")

# 不可迭代
try:
    for f in float_example:
        print(f)
except TypeError as e:
    print(e)

# 长度
try:
    len(float_example)
except TypeError as e:
    print(e)

# 索引操作
try:
    print(float_example[0])
except TypeError as e:
    print(e)

# 常用方法
print(f"Exponentiation: {float_example**2}")
print(f"Square root: {float_example**0.5}")

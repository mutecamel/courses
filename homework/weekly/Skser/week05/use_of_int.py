# 整数 (int)
int_example = 42

# 使用内置函数检视对象
print(f"ID: {id(int_example)}")
print(f"Type: {type(int_example)}")
print(f"Is instance of int: {isinstance(int_example, int)}")
print(f"Attributes and methods: {dir(int_example)}")
print(f"Integer representation: {str(int_example)}")

# 数学运算符支持
result = int_example + 10
print(f"Addition: {result}")

# 判断相等
assert int_example == 42, "Integers are not equal"

# 比较运算符支持
another_int = 50
if another_int > int_example:
    print("another_int is greater than int_example")

# 布尔值判断
zero_int = 0
non_zero_int = 42
print(f"Zero integer evaluates to: {bool(zero_int)}")
print(f"Non-zero integer evaluates to: {bool(non_zero_int)}")

# 不可迭代
try:
    for i in int_example:
        print(i)
except TypeError as e:
    print(e)

# 长度
try:
    len(int_example)
except TypeError as e:
    print(e)

# 索引操作
try:
    print(int_example[0])
except TypeError as e:
    print(e)

# 常用方法
print(f"Binary: {bin(int_example)}")
print(f"Hexadecimal: {hex(int_example)}")
print(f"Octal: {oct(int_example)}")

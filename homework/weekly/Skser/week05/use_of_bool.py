# 布尔值 (bool)
bool_example = True

# 使用内置函数检视对象
print(f"ID: {id(bool_example)}")
print(f"Type: {type(bool_example)}")
print(f"Is instance of bool: {isinstance(bool_example, bool)}")
print(f"Attributes and methods: {dir(bool_example)}")
print(f"Boolean representation: {str(bool_example)}")

# 数学运算符支持
result = bool_example + 1
print(f"Addition: {result}")

# 判断相等
assert bool_example == True, "Booleans are not equal"

# 比较运算符支持
another_bool = False
if another_bool < bool_example:
    print("another_bool is less than bool_example")

# 布尔值判断
true_value = True
false_value = False
print(f"True value evaluates to: {bool(true_value)}")
print(f"False value evaluates to: {bool(false_value)}")

# 不可迭代
try:
    for b in bool_example:
        print(b)
except TypeError as e:
    print(e)

# 长度
try:
    len(bool_example)
except TypeError as e:
    print(e)

# 索引操作
try:
    print(bool_example[0])
except TypeError as e:
    print(e)

# 常用方法
print(f"Not operation: {not bool_example}")

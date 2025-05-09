# 元组 (tuple)
tuple_example = (1, 2, 3, 4, 5)

# 使用内置函数检视对象
print(f"ID: {id(tuple_example)}")
print(f"Type: {type(tuple_example)}")
print(f"Is instance of tuple: {isinstance(tuple_example, tuple)}")
print(f"Attributes and methods: {dir(tuple_example)}")
print(f"Tuple representation: {str(tuple_example)}")

# 数学运算符支持
try:
    result = tuple_example + (6, 7)
    print(f"Concatenation: {result}")
except TypeError as e:
    print(e)

# 判断相等
assert tuple_example == (1, 2, 3, 4, 5), "Tuples are not equal"

# 比较运算符支持
another_tuple = (1, 2, 3, 4, 6)
if another_tuple > tuple_example:
    print("another_tuple is greater than tuple_example")

# 布尔值判断
empty_tuple = ()
non_empty_tuple = (1, 2, 3)
print(f"Empty tuple evaluates to: {bool(empty_tuple)}")
print(f"Non-empty tuple evaluates to: {bool(non_empty_tuple)}")

# 可迭代性
for item in tuple_example:
    print(item, end=" ")
print()

# 长度
print(f"Length of tuple_example: {len(tuple_example)}")

# 索引操作
print(f"First element: {tuple_example[0]}")
print(f"Last element: {tuple_example[-1]}")

# 常用方法
count_of_3 = tuple_example.count(3)
index_of_4 = tuple_example.index(4)
print(f"Count of 3: {count_of_3}")
print(f"Index of 4: {index_of_4}")

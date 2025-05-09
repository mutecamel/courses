# 列表 (list)
list_example = [1, 2, 3, 4, 5]

# 使用内置函数检视对象
print(f"ID: {id(list_example)}")
print(f"Type: {type(list_example)}")
print(f"Is instance of list: {isinstance(list_example, list)}")
print(f"Attributes and methods: {dir(list_example)}")
print(f"List representation: {str(list_example)}")

# 数学运算符支持
try:
    result = list_example + [6, 7]
    print(f"Concatenation: {result}")
except TypeError as e:
    print(e)

# 判断相等
assert list_example == [1, 2, 3, 4, 5], "Lists are not equal"

# 比较运算符支持
another_list = [1, 2, 3, 4, 6]
if another_list > list_example:
    print("another_list is greater than list_example")

# 布尔值判断
empty_list = []
non_empty_list = [1, 2, 3]
print(f"Empty list evaluates to: {bool(empty_list)}")
print(f"Non-empty list evaluates to: {bool(non_empty_list)}")

# 可迭代性
for item in list_example:
    print(item, end=" ")
print()

# 长度
print(f"Length of list_example: {len(list_example)}")

# 索引操作
print(f"First element: {list_example[0]}")
print(f"Last element: {list_example[-1]}")

# 常用方法
list_example.append(6)
print(f"After append: {list_example}")
list_example.remove(3)
print(f"After remove: {list_example}")
list_example.sort(reverse=True)
print(f"After sort: {list_example}")

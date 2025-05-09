# 集合 (set)
set_example = {1, 2, 3, 4, 5}

# 使用内置函数检视对象
print(f"ID: {id(set_example)}")
print(f"Type: {type(set_example)}")
print(f"Is instance of set: {isinstance(set_example, set)}")
print(f"Attributes and methods: {dir(set_example)}")
print(f"Set representation: {str(set_example)}")

# 数学运算符支持
try:
    result = set_example | {6, 7}
    print(f"Union: {result}")
except TypeError as e:
    print(e)

# 判断相等
assert set_example == {1, 2, 3, 4, 5}, "Sets are not equal"

# 比较运算符支持
try:
    if set_example > {1, 2, 3, 4, 6}:
        print("set_example is greater than {1, 2, 3, 4, 6}")
except TypeError as e:
    print(e)

# 布尔值判断
empty_set = set()
non_empty_set = {1, 2, 3}
print(f"Empty set evaluates to: {bool(empty_set)}")
print(f"Non-empty set evaluates to: {bool(non_empty_set)}")

# 可迭代性
for item in set_example:
    print(item, end=" ")
print()

# 长度
print(f"Length of set_example: {len(set_example)}")

# 索引操作
try:
    print(set_example[0])
except TypeError as e:
    print(e)

# 常用方法
set_example.add(6)
print(f"After add: {set_example}")
set_example.remove(3)
print(f"After remove: {set_example}")
union_set = set_example.union({7, 8})
intersection_set = set_example.intersection({4, 5, 6})
difference_set = set_example.difference({1, 2})
symmetric_difference_set = set_example.symmetric_difference({1, 2, 6, 7})
print(f"Union: {union_set}")
print(f"Intersection: {intersection_set}")
print(f"Difference: {difference_set}")
print(f"Symmetric Difference: {symmetric_difference_set}")

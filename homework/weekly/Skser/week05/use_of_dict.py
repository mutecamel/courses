# 字典 (dict)
dict_example = {"name": "Alice", "age": 25}

# 使用内置函数检视对象
print(f"ID: {id(dict_example)}")
print(f"Type: {type(dict_example)}")
print(f"Is instance of dict: {isinstance(dict_example, dict)}")
print(f"Attributes and methods: {dir(dict_example)}")
print(f"Dict representation: {str(dict_example)}")

# 数学运算符支持
try:
    result = dict_example + {"city": "Wonderland"}
    print(f"Concatenation: {result}")
except TypeError as e:
    print(e)

# 判断相等
assert dict_example == {"name": "Alice", "age": 25}, "Dictionaries are not equal"

# 比较运算符支持
try:
    if dict_example > {"name": "Bob", "age": 25}:
        print("dict_example is greater than {'name': 'Bob', 'age': 25}")
except TypeError as e:
    print(e)

# 布尔值判断
empty_dict = {}
non_empty_dict = {"key": "value"}
print(f"Empty dictionary evaluates to: {bool(empty_dict)}")
print(f"Non-empty dictionary evaluates to: {bool(non_empty_dict)}")

# 可迭代性
for key in dict_example:
    print(key, dict_example[key])

# 长度
print(f"Length of dict_example: {len(dict_example)}")

# 索引操作
print(f"Value of 'name': {dict_example['name']}")

# 常用方法
dict_example["city"] = "Wonderland"
print(f"After adding city: {dict_example}")
del dict_example["age"]
print(f"After deleting age: {dict_example}")
keys = dict_example.keys()
values = dict_example.values()
items = dict_example.items()
print(f"Keys: {keys}")
print(f"Values: {values}")
print(f"Items: {items}")

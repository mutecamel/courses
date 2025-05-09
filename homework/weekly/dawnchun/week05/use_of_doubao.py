# 1. int 类型
num1 = 5
num2 = 3

# 数学运算符支持
print("int 数学运算：")
print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} * {num2} = {num1 * num2}")
print(f"{num1} ** {num2} = {num1 ** num2}")
print(f"{num1} / {num2} = {num1 / num2}")
print(f"{num1} // {num2} = {num1 // num2}")
print(f"{num1} % {num2} = {num1 % num2}")

# 判断相等
print(f"int 判断相等：{num1 == num2}")

# 比较运算符支持
print("int 比较运算：")
print(f"{num1} > {num2}: {num1 > num2}")
print(f"{num1} < {num2}: {num1 < num2}")
print(f"{num1} >= {num2}: {num1 >= num2}")
print(f"{num1} <= {num2}: {num1 <= num2}")

# 布尔值映射
print(f"int 布尔值映射：bool({num1}) = {bool(num1)}, bool(0) = {bool(0)}")

# 不可迭代
try:
    for i in num1:
        print(i)
except TypeError:
    print("int 不可迭代")

# 不支持返回长度
try:
    print(len(num1))
except TypeError:
    print("int 不支持返回长度")

# 不支持索引操作
try:
    print(num1[0])
except TypeError:
    print("int 不支持索引操作")

# 常用方法
print(f"int 常用方法：{dir(int)}")


# 2. float 类型
float1 = 5.0
float2 = 3.0

# 数学运算符支持
print("\nfloat 数学运算：")
print(f"{float1} + {float2} = {float1 + float2}")
print(f"{float1} - {float2} = {float1 - float2}")
print(f"{float1} * {float2} = {float1 * float2}")
print(f"{float1} ** {float2} = {float1 ** float2}")
print(f"{float1} / {float2} = {float1 / float2}")
print(f"{float1} // {float2} = {float1 // float2}")
print(f"{float1} % {float2} = {float1 % float2}")

# 判断相等
print(f"float 判断相等：{float1 == float2}")

# 比较运算符支持
print("float 比较运算：")
print(f"{float1} > {float2}: {float1 > float2}")
print(f"{float1} < {float2}: {float1 < float2}")
print(f"{float1} >= {float2}: {float1 >= float2}")
print(f"{float1} <= {float2}: {float1 <= float2}")

# 布尔值映射
print(f"float 布尔值映射：bool({float1}) = {bool(float1)}, bool(0.0) = {bool(0.0)}")

# 不可迭代
try:
    for i in float1:
        print(i)
except TypeError:
    print("float 不可迭代")

# 不支持返回长度
try:
    print(len(float1))
except TypeError:
    print("float 不支持返回长度")

# 不支持索引操作
try:
    print(float1[0])
except TypeError:
    print("float 不支持索引操作")

# 常用方法
print(f"float 常用方法：{dir(float)}")


# 3. str 类型
str1 = "hello"
str2 = "world"

# 数学运算符支持
print("\nstr 数学运算：")
print(f"{str1} + {str2} = {str1 + str2}")
print(f"{str1} * 3 = {str1 * 3}")

# 判断相等
print(f"str 判断相等：{str1 == str2}")

# 比较运算符支持
print("str 比较运算：")
print(f"{str1} > {str2}: {str1 > str2}")
print(f"{str1} < {str2}: {str1 < str2}")
print(f"{str1} >= {str2}: {str1 >= str2}")
print(f"{str1} <= {str2}: {str1 <= str2}")

# 布尔值映射
print(f"str 布尔值映射：bool({str1}) = {bool(str1)}, bool('') = {bool('')}")

# 可迭代
print("str 迭代：")
for char in str1:
    print(char)

# 支持返回长度
print(f"str 长度：{len(str1)}")

# 支持索引操作
print(f"str 索引操作：{str1[0]}")

# 常用方法
print(f"str 常用方法：{dir(str)}")


# 4. list 类型
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# 数学运算符支持
print("\nlist 数学运算：")
print(f"{list1} + {list2} = {list1 + list2}")
print(f"{list1} * 2 = {list1 * 2}")

# 判断相等
print(f"list 判断相等：{list1 == list2}")

# 比较运算符支持
print("list 比较运算：")
print(f"{list1} > {list2}: {list1 > list2}")
print(f"{list1} < {list2}: {list1 < list2}")
print(f"{list1} >= {list2}: {list1 >= list2}")
print(f"{list1} <= {list2}: {list1 <= list2}")

# 布尔值映射
print(f"list 布尔值映射：bool({list1}) = {bool(list1)}, bool([]) = {bool([])}")

# 可迭代
print("list 迭代：")
for item in list1:
    print(item)

# 支持返回长度
print(f"list 长度：{len(list1)}")

# 支持索引操作
print(f"list 索引操作：{list1[0]}")

# 常用方法
print(f"list 常用方法：{dir(list)}")


# 5. dict 类型
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

# 不支持大部分数学运算符
try:
    print(dict1 + dict2)
except TypeError:
    print("\ndict 不支持 + 运算符")

# 判断相等
print(f"dict 判断相等：{dict1 == dict2}")

# 比较运算符不支持（Python 3 中）
try:
    print(dict1 > dict2)
except TypeError:
    print("dict 不支持比较运算符")

# 布尔值映射
print(f"dict 布尔值映射：bool({dict1}) = {bool(dict1)}, bool({}) = {bool({})}")

# 可迭代
print("dict 迭代：")
for key in dict1:
    print(key)

# 支持返回长度
print(f"dict 长度：{len(dict1)}")

# 支持索引操作（通过键）
print(f"dict 索引操作：{dict1['a']}")

# 常用方法
print(f"dict 常用方法：{dir(dict)}")


# 6. set 类型
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# 数学运算符支持（部分）
print("\nset 数学运算：")
print(f"{set1} | {set2} = {set1 | set2}")  # 并集
print(f"{set1} & {set2} = {set1 & set2}")  # 交集
print(f"{set1} - {set2} = {set1 - set2}")  # 差集

# 判断相等
print(f"set 判断相等：{set1 == set2}")

# 比较运算符支持（部分）
print("set 比较运算：")
print(f"{set1} > {set2}: {set1 > set2}")  # 真超集判断
print(f"{set1} < {set2}: {set1 < set2}")  # 真子集判断
print(f"{set1} >= {set2}: {set1 >= set2}")  # 超集判断
print(f"{set1} <= {set2}: {set1 <= set2}")  # 子集判断

# 布尔值映射
print(f"set 布尔值映射：bool({set1}) = {bool(set1)}, bool(set()) = {bool(set())}")

# 可迭代
print("set 迭代：")
for item in set1:
    print(item)

# 支持返回长度
print(f"set 长度：{len(set1)}")

# 不支持索引操作
try:
    print(set1[0])
except TypeError:
    print("set 不支持索引操作")

# 常用方法
print(f"set 常用方法：{dir(set)}")
    
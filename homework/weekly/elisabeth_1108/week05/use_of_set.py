# 创建集合
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# 集合操作
# 并集
union_set = set1.union(set2)
print("并集:", union_set)

# 交集
intersection_set = set1.intersection(set2)
print("交集:", intersection_set)

# 差集
difference_set = set1.difference(set2)
print("差集:", difference_set)

# 添加元素
set1.add(5)
print("添加元素后的set1:", set1)

# 删除元素
set1.remove(5)
print("删除元素后的set1:", set1)

try:
    s = [1, [2], 3, 4]
except TypeError as e:
    print(e)

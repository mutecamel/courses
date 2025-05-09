# 集合 (set)
# 创建集合
my_set = {1, 2, 3, 'apple', 'banana'}
print("创建的集合:", my_set)

# 添加元素到集合
my_set.add('cherry')
print("添加元素后的集合:", my_set)

# 从集合中移除元素
my_set.remove('apple')
print("移除元素后的集合:", my_set)

# 集合的交集操作
set1 = {1, 2, 3}
set2 = {3, 4, 5}
intersection = set1.intersection(set2)
print("集合 set1 和 set2 的交集:", intersection)
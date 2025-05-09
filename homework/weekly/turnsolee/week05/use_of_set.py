s = {3, 5, 8}
print(s)
print(type(s))

# 尝试创建一个包含列表的集合，由于列表是可变类型，不能作为集合元素，会触发TypeError
try:
    s = {3, [5], 8}
except TypeError as e:
    print(e)

# 创建另一个集合q
q = {3, 4, 6, 4, 7, 6}
print(q)
print(type(q))

# 再次创建集合s
s = {6, 4, 7, 4, 4, 7}
print(s)
# 检查整数4是否在集合s中，返回True或False
print(4 in s)
# 检查集合s是否是自身的子集，返回True或False
print(s <= s)

# 创建集合s2
s2 = {7, 4, 7}
print(s2)
# 求集合s和s2的并集，返回一个新集合
print(s | s2)
# 检查集合s和s2是否相等，返回True或False
print(s == s2)

t = (1, 'a', 3.14)
print(t)
print(type(t))

# 访问元组t的第一个元素（索引从0开始）并打印
print(t[0])
# 访问元组t的第二个元素并打印
print(t[1])
# 访问元组t的第三个元素并打印
print(t[2])

# 尝试修改元组t的第一个元素，元组是不可变类型，会触发TypeError
try:
    t[0] = 9
except TypeError as e:
    print(e)

# 创建一个空字典d
d = {}
# 向字典d中添加键值对，键为'abc'，值为5
d['abc'] = 5
# 向字典d中添加键值对，键为7，值为100
d[7] = 100

# 创建一个列表q
q = [3, 1]
# 尝试将列表q作为键添加到字典d中，列表是可变类型，不可哈希，会触发TypeError
try:
    d[q] = 21
except TypeError as e:
    print(e)

# 创建一个元组t，包含三个元素：整数100、元组(3)
t = (100, (3))
# 向字典d中添加键值对，键为元组t，值为21
d[t] = 21
# 打印字典d的内容
print(d)

# 访问字典d中键为(3, 1)的值并打印
print(d[(3, 1)])

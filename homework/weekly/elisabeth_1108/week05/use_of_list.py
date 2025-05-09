# 创建一个列表
my_list = [1, 2, 3, 4, 5]

# 访问元素
print(my_list[0])  # 输出 1
print(my_list[-1])  # 输出 5，-1 表示最后一个元素

# 修改元素
my_list[0] = 10
print(my_list)  # 输出 [10, 2, 3, 4, 5]

# 添加元素
my_list.append(6)
print(my_list)  # 输出 [10, 2, 3, 4, 5, 6]

# 删除元素
del my_list[0]
print(my_list)  # 输出 [2, 3, 4, 5, 6]

# 遍历列表
for item in my_list:
    print(item)


# 列表推导式
words = ['hello', 'world', 'python']
upper_words = [word.upper() for word in words]
print(upper_words)

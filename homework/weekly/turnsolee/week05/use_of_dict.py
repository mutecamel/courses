d = {'a': 1, 'bb': 5, 'cat': 3}
print(d)
# 打印输出字典d的类型
print(type(d))

# 遍历字典d，这里a代表字典的键，依次打印出字典的键
for a in d:
    print(a)

# 利用字典的keys()方法遍历字典d的键，和上面直接遍历字典效果相同，依次打印出字典的键
for a in d.keys():
    print(a)

# 利用字典的values()方法遍历字典d的值，依次打印出字典的值
for a in d.values():
    print(a)

# 使用列表推导式，将字典d的键值对以元组形式提取出来组成列表，赋值给变量l
l = [a for a in d.items()]
# 打印输出列表l
print(l)

# 遍历字典d的键值对，k代表键，v代表值，依次打印出键和值
for k, v in d.items():
    print(k, v)

breakpoint()

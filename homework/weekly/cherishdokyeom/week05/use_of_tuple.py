a = (9, "friends", 10)  # 元祖对象不支持修改，但列表支持
print(a)
print(type(a))
print(a[0])
print(a[1])
print(a[2])

try:  # 元祖对象不支持修改，但列表支持
    a[0] = 5
except TypeError as e:
    print(e)
# 元祖的括号在不产生歧义的情况下可以省略

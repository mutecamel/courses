##字典也是一种容器，没有顺序，更精简，耗费内存更少，可以尝试用字符串找到某一个值
##字典包含键值对
d = {"apple": 1, "boy": 2, "cat": 3}
print(d, type(d))

##字典可以循环
for a in d:
    print(a)
##显示字典中字符串所代表的值
for a in d:
    print(d[a])
##第二种方法
for a in d.values():
    print(a)

l = [a for a in d.items()]
print(l)

for m, n in d.items():
    print(m, n)
##空字典被显示为False
assert not {}

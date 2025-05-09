##元组和列表相似，也可以提取，元组元素不可以修改
t = (17, "seventeen", 5.26)
print(t, type(t))
print(t[0])
print(t[1])
try:
    t[0] = 9
except TypeError as e:
    print(e)
###可修改的对象不可以作为字典里的键
d = {}
d["seven"] = 17
d[5] = 25
print(d)

q = [5, 26]
try:
    d[q] = 17
except TypeError as e:
    print(e)  ##列表作为可变元素就不能作为字典里的键
print(d)

m = (5, 26)
d[m] = 17
print(d)
print(d[5, 26])  ##提取字典中键所代表的值，[]中是该元组所包含的键

##没有语法的歧义的时候可以省略元组的圆括号
t = 0, 5, 2, 6
print(t, type(t))

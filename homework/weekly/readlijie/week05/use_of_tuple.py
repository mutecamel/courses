t = (1, "a", 3.12, "gg", 3456)
print(t)  #   (1, 'a', 3.12, 'gg', 3456)
print(type(t))  #   <class 'tuple'>  元组不可变 不可修改

print(t[0])
print(t[1])
print(t[2])
print(t[3])
print(t[4])

try:
    t[0] = 9
except TypeError as e:
    print(e)

d = {}
d["beef"] = 5  #  可修改对象不能作为箭
d[34] = 388
d["apple"] = 388
q = [3, 7790790]

try:
    d[q] = 668
except TypeError as e:
    print(e)

t = (3, 456, 77, 7979)  #   元组可以作为箭
d[t] = 999
print(d)  #  {'beef': 5, 34: 388, 'apple': 388, (3, 456, 77, 7979): 999}
print(d[3, 456, 77, 7979])

t = 1, 33, 4, 5, 6, 7, 8, 8897  # 字典序 先比较第一个值
print(t)
print(type(t))  #   <class 'tuple'>

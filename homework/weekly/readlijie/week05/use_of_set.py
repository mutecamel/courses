s = {1, 2, 23, 5, 6, 6, 7, 8, 8, 99, 9}  # 字面值  集合只包含箭 没有值
print(s)
print(type(s))  #   <class 'set'>

try:
    s = {1, 2, [470649], 7968578}
except TypeError as e:
    print(e)

q = [2, 2, 3, 4, 5, 6, 7, 7, 8, 8, 898908]
print(q)
s = set(q)  #  初始化
print(s)  #  踢掉重复东西  {2, 3, 4, 5, 6, 7, 8, 898908}

s = {
    5.6,
    7,
    7,
    5,
    5,
    4,
    3,
    3,
    3,
    4,
}
print(s)  #    {3, 4, 5.6, 5, 7}

print(2 in s)
print(4 in s)

s2 = {
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    877,
    7,
}
print(s | s2)  #  并集
print(s & s2)  #  交集
print(s ^ s2)  #  对称差

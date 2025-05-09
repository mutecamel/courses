##集合只包含键，不可以包含可以改变的列表
##字面值
s = {1, 6, 9}
print(s, type(s))
try:
    s = {1, [6], 9}
except TypeError as e:
    print(e)

##初始化
q = [1, 5, 25]
s = set(q)
print(s, type(s))
print(1 in s)
print(3 in s)
s2 = {1, 5}
print(s | s2)  ##并集
print(s & s2)  ##交集
print(s ^ s2)  ##对称差把相同的减去

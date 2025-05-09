s = {1, 4, 8}
print(s)
print(type(s))

try:
    s = {1, [4], 7}  # 会报错，因为列表是一个可变的值
except TypeError as e:
    print(e)

# 会去掉重复值
q = [1, 2, 1, 2, 5, 1]
print(q)
s = set(q)
print(s)

s = {5, 2, 1, 2, 2, 1}  # 可以做并交补
print(s)
print(2 in s)
print(3 in s)

# 并集和交集 对称差,不存在补集
s2 = {3, 2, 3}
print(s | s2)
print(s & s2)
print(s ^ s2)


breakpoint()

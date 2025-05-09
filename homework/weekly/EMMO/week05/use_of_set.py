a = {1, 4, 7, 2, 5, 8}
print(a)
print(type(a))

try:
    a = {1, 2, [3]}
except TypeError as e:
    print(e)

b = [1, 2, 3, 4, 5, 6]
print(b)
print(type(b))
a = set(b)
print(a)
print(type(a))

a = {1, 1, 2, 3, 4, 5, 1, 2, 3, 8}
print(a)
print(1 in a)
print(2 in a)

a1 = {6, 9}
print(a | a1)  # 并集
print(a & a1)  # 交集

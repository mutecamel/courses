cl = [1, 5, "abc"]
print(cl)

print(cl[0])

try:
    print(cl[3])
except IndexError as e:
    print(e)

a = [2, 3]
print(cl + a)

print(cl + a == a + cl)  ##不支持-运算 支持*运算
print(a * 2)

b = a * 2
print(b)
a[0] = 3
print(a)
print(b)

a = [1, 2]
b = [a] * 2
print(b)
a[0] = 3
print(a)
print(b)

a = [2, 5, 3]
b = [i**2 for i in a]  ##运算式
print(b)

a = [1, 2]
b = [a] * 2
print(b)
x = a.append(4)
print(a)
print(b)
print(x)

l = [1, 4, "abc"]  # 列表就是一个容器
print(l)

print(l[0])
print(1[1])
print(l[2])

try:
    print(l[3])
except IndexError as e:
    print(e)

print(l[-1])
print(l[-1][1])

# 可以加减
a = [2, 3]
b = [5]
print(a + b)
print(b + a)
print(a + b == b + a)

a = [2, 5]
b = [5]
try:
    print(a - b)
except TypeError as e:
    print(e)

a = [2, 5]
print(a * 3)

a = [2, 5]
b = a * 3
print(f"{b=}")
a[0] = 9
print(a)
print(b)

a = [2, 5]
b = [a] * 3
print(f"{b=}")
a[0] * 9
print(a)
print(b)
# 列表推导式，也可以嵌套
a = [2, 5, 3]
b = [i**2 for i in a]
print(b)
b = [i**2 for i in a if i < 4]
print(b)

a = [2, 5]
b = [a] * 3
print(f"{b=}")
x = a.append(4)
print(x)
print(a)
print(b)
breakpoint()  # import wat    wat / a   查看关于它的命令

a = [9, 10, "zu"]  # 可以不一样，但最好一样
print(a)

print(a[0])
print(a[1])
print(a[2])

# print(a[3])
try:
    print(a[3])
except IndexError as e:
    print(e)

print(a[-1])  # 最后一个
print(a[-1][-1])
n = [10, 9, "mingyu"]
print(a + n)
print(n + a)
print(a + n == n + a)  # 结果为False

x = [9, 10]  # 列表不支持减法
y = [10]
try:
    print(x - y)
except TypeError as e:
    print(e)

print(x * 2)  # 列表支持乘法

b = x * 3
print(f"{b=}")
x[0] = 1  # 重新赋值
print(x)
print(b)

m = [9, 10]
n = [m] * 3
print(f"{n=}")
m[0] = 10
print(m)
print(n)

m = [1, 9, 10]
n = [i**2 for i in m]
print(n)

p = [i**2 for i in m if i < 10]  # 起到过滤的作用，后面为True才展示
print(p)

m = [9, 10]
n = [m] * 3
print(f"{n=}")
x = m.append(17)  # 添加17到m
print(x)
print(m)
print(n)
# breakpoint()

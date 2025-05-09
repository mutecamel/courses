##列表→容器，里面包含不同的元素
l = [5, 6, "seventeen"]
print(l)
print(l[0])
print(l[1])
print(l[2])
print(l[-1][3])


##列表可以支持加法，也可以比较大小
a = ["seven", "teen"]
b = [5, 6]
print(a + b)
print(b + a)  ##没有加法交换律
c = [5]
try:
    print(b - c)
except TypeError as e:
    print(e)  ##列表不支持减法
print(c * 5)

a = [5, 6]
b = a * 2  ##这里b是引用a生成一个新的列表
a[0] = 6
print(a)
print(b)


a = [5, 6]
b = [a] * 2
print(f"{b=}")  ##b还是指向a
a[0] = 6  ##将a的第一个元素赋值为6
print(a)
print(b)
##推导式
a = [1, 2, 3]
b = [i * 2 for i in a]
print(b)
b = [i * 2 for i in a if i >= 2]  ##先计算if如果if为Ture再进行下一步
print(b)

a = [5, 6]
b = [a] * 2
print(f"{b=}")
x = a.append(4)  ##使用append向列表中加入元素
print(x)
print(a)
print(b)  ##b也会改变

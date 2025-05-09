l = [1, 5, "abc"]
print(l)

try:
    print(l[0])  # 打印第一个元素
    print(l[1])  # 打印第二个元素
    print(l[2])  # 打印第三个元素
    print(l[3])  # 故意越界，触发IndexError
except IndexError as e:
    print("list index out of range")

# 切片操作
print(l[:2])  # 取前两个元素
print(l[1:])  # 取从第二个元素到末尾的元素

# 列表拼接
a = [2, 5]
b = ['a', 'c']
print(a + b)  # 拼接两个列表
print(b + a)  # 改变顺序

# 检查列表拼接是否满足交换律（实际不满足）
print(a + b == b + a)

# 尝试列表相减（会触发TypeError，因为列表不支持减法运算）
try:
    print(a - b)
except TypeError as e:
    print("unsupported operand type(s) for -: 'list' and 'list'")

# 列表重复
a = [2, 5]
print(a * 3)  # 列表重复3次

# 元素修改
a = [2, 5]
b = a * 3
b[0] = 9  # 修改第一个元素
print(b)

# 遍历列表
a = [2, 5, 8]
for i in a:
    print(i)

# 列表推导式
a = [2, 5, 8]
b = [i * 2 for i in a if i < 8]  # 对小于8的元素乘以2
print(b)

# 使用列表方法 - append
a = [2, 5]
x = a.append(4)  # append方法返回值为None，这里只是展示调用
print(x)
print(a)

# 使用列表方法 - extend
a = [2, 5]
a.extend([7, 9])  # 在列表末尾添加多个元素
print(a)

# 使用列表方法 - pop
a = [2, 5, 7]
popped = a.pop()  # 弹出并返回最后一个元素
print(popped)
print(a)

breakpoint()

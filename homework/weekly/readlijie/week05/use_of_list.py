l = [1, 5, "abcd", 79, "big"]
print(l)  #  [1, 5, 'abcd', 79, 'big']

print(l[0])
print(l[1])
print(l[2])

try:
    print(l[5])
except IndexError as e:
    print(e)

print(l[-1])
print(l[-4])
print(l[2][2])

a = [2, 55, 66]
b = ["ss", "dd"]
print(a + b)
print(b + a)
print(a + b == b + a)  #   False

a = [2, 5, 6]
b = [2, 5]

try:
    print(a - b)
except TypeError as e:
    print(e)

a = [3, 4, 5]
print(a * 12)

a = [2, 5]
a[0] = 7
b = a * 3
print(a)
print(b)  # [7, 5, 7, 5, 7, 5] 个人理解此处与是否先对a第一个数重新赋值有关

a = [2, 5]
b = a * 3
print(f"{b=}")  #  b=[2, 5, 2, 5, 2, 5]
a[0] = 7
print(a)
print(b)  #   [2, 5, 2, 5, 2, 5]

a = [2, 5]
b = [a] * 3
print(f"{b=}")  #  b=[[2, 5], [2, 5], [2, 5]]
a[0] = 9
print(a)
print(b)  #   [[9, 5], [9, 5], [9, 5]]

a = [3, 6, 9]
b = [i**2 for i in a]  #  推导式
print(b)  #   [9, 36, 81]
c = [i**3 + 6 - 1 / 2 for i in a]
print(c)  #   [32.5, 221.5, 734.5]
b = [i**3 - 1 for i in a if i > 3.112]  # 加条件筛选
print(b)  #    [215, 728]

a = [2, 5, 9, "yuyu"]
b = [a] * 3
print(f"{b=}")
x = a.append("aaa")
print(x)  #  没有返回值
print(a)
print(b)

a = [2, 5]
b = [a] * 3
print(f"{b=}")
x = a.append(4)
print(x)  #   None
print(a)  #   [2, 5, 4]
print(b)  #   [[2, 5, 4], [2, 5, 4], [2, 5, 4]]
breakpoint()

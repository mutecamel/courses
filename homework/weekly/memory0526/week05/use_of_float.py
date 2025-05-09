##字符串转化的浮点值和直接输入的浮点值相等
import random

x = 2.25
y = float("2.25")
assert x == y
z = x / 4  ##另外整数、整数也可以得到浮点数
print(z, type(z))

##函数的返回值也可以是float
x = random.random()  ##random，0-1均匀抽取的随机数，import random按照规范应该置顶
print(x)
##浮点数0.0为false，不要用浮点判断是否相等，可能存在四舍五入的误差
assert not 0.0
na = float("nan")  ##nan为缺失值，和任何数运算都是nan
print(na + 5)

pinf = float("inf")  ##正无穷
print(pinf)
print(3.12e2)  ##科学计数法
print(pinf > 3e100)
print(pinf * 0)

ninf = float("-inf")  ##负无穷
print(ninf < -1e100)

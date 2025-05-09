# 元组和列表很相似
t = (1, "a", 3.14)
print(t)
print(type(t))

print(t[0])
print(t[1])
print(t[2])

# 验证属性
# 1.对数学运算符 (+、-、*、/、//、%、@) 有没有支持
# 仅支持+、*
t1 = (1, 2)
t2 = (3, 4)
print(t1 + t2)  # 输出：(1, 2, 3, 4)
t = (1, 2)
print(t * 3)  # 输出：(1, 2, 1, 2, 1, 2)

# 不支持-、/、//、%、@
# t = (1, 2)
# print(t - (1,))  # TypeError: unsupported operand type(s) for -: 'tuple' and 'tuple'
# print(t / 2)  # TypeError: unsupported operand type(s) for /: 'tuple' and 'int'

# 2.如何判断相等 (==)
assert t == (1, 2)

# 3.对于比较运算符 (>、<、>=、<=) 有没有支持
# 相同长度，逐元素比较
print((1, 2, 3) < (1, 2, 4))  # True（因为 3 < 4）
print((1, 2, 3) > (1, 1, 5))  # True（因为 2 > 1，后续不比较）

# 不同长度
print((1, 2) < (1, 2, -1))  # True（前两元素相同，左侧更短）
print((1, 2, 3) > (1, 2))  # True（前两元素相同，右侧更短）

# 合法比较（同类型元素）
print(("a", 2) < ("b", 1))  # True（"a" < "b"）

# 非法比较（不同类型元素）
# print((1, "a") < ("b", 2))    # TypeError: '<' not supported between 'int' and 'str'

# 递归比较嵌套结构
print((1, (2, 3)) < (1, (2, 4)))  # True（(2, 3) < (2, 4)）


# 4.什么值被当作 True，什么值被当作 False
t = ()
print(bool(t))  # False

t1 = (0,)
t2 = (False,)
t3 = ("", None)
print(bool(t1), bool(t2), bool(t3))  # 全部输出 True

# 5是否支持返回长度 (len)
my_tuple = (10, 20, 30, 40, 50)
length = len(my_tuple)
print(length)  # 输出：5

# 6.是否 (如何) 支持索引操作 (subscription) ([] 运算符)
my_tuple = (10, 20, 30, 40, 50)
print(my_tuple[0])  # 输出：10（第一个元素）
print(my_tuple[-1])  # 输出：50（最后一个元素）

# 7拥有哪些常用方法 (method) 可供调用 (() 运算符)
t = (1, 2, 2, 3, 2)
print(t.count(2))  # 输出：3


t = ("a", "b", "c", "b")
print(t.index("b"))  # 输出：1
print(t.index("b", 2))  # 输出：3（从索引2开始搜索）


# 元组不支持赋值
try:
    t[0] = 9
except TypeError as e:
    print(e)

breakpoint()  # import wat            wat / t

# 字典里的键是不可变的，列表算不了哈希值，因为是可变的值
d = {}
d["abc"] = 5
d[7] = 100
q = [3, 1]

try:
    d[q] = 21
except TypeError as e:
    print(e)

t = (3, 1)
d[t] = 21
print(d)
print(d[3, 2])

# 元组可以省略圆括号，但是语法不存在歧义
t = 1, 4, 0, 2
print(t)
print(type(t))

a = "str验证,在这是一个字符串"
a1 = "str验证,在这是一个字符串"
b = "另一个字符串"
print(a)
x = id(a)
print(x)
print(id(a1))
y = id(b)
print(y)
c = [100, 65]
d = [55, 989]
print(id(c))
print(id(d))
print(type(a))
print(type(c))
print(type(x))
print(isinstance(a, str))  # 如果a是str,则为true,否则为false
print(isinstance(c, str))
print(dir(a))
print(str(c))
try:
    assert isinstance(c, str)  # 如果报错会直接退出,未报错则直接
except AssertionError:
    print("报错啦")
print("end")

# 实例(字面值)
u = "iiii"
assert type(u) is str

print("f-string")
x1 = "lingling"
s1 = f"name: {x1}"
print(s1)

s = "a\tb"  # 空格的
print("TAB", s)

s = "这个是干嘛的\n让我来试试"  # 换行的
print("New Line", s)

# 新东西
s = """这个又是干嘛的
输出什么东西
    缩进一下试试
来个数字7456546
"""
print(s)  # 怎么输入的就怎么输出的

# 初始化
print("chushihua")
s = str()
print(s)
s = str([10086, 7461, 63])
print(s)

# 运算值
s = "+"
s = s * 19
print(s)

# 索引值
s = "apple"
assert s[1] == "p"  # python的字符串是从0开始计算的!!
print(s[:3])

# 返回值
s = "dianrANdahai"
d = s.upper()
print(d)

# 运算符号
g = "zhekfoa"
h = "5613"
print(g + h)

s = "***-***"
s = s * 8
print(s)

assert "aaabc" > "AAABC"
print("abc" > "123")

s = "dianrandahai"
for c in s:
    print(c)
print(len(s))

s = "jisd:ivsud:odv"
print(s.split(":"))

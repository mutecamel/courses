# 1.字面值
print("字面值")
s = "university"
print(s)
print(isinstance(s, str))
assert type(s) is str

print("f-string")
x = "Tom"
s = f"name: {x}"
print(s)

s = "a\tb"
print("pig", s)

s = "ccc\nddd"
print("cat", s)


# raw-string,translate,multi-line

s = """xyz
abc
   eee
aaa
"""
print(s)

# 2.初始化
print("初始化")
s = str()
print(s)
s = str([1, 2, 3])
print(s)

assert str([1, 2, 3]) == "[1, 2, 3]"
assert str(1.1 + 2.2) != "3.3"
assert str() == ""

# 出现报错的话，利用pdb检查
# python -m pdb use_of_str.py
# c
# l .
# p str()


# 3.运算值
s = "$"
x = id(s)
s = s * 10
y = id(s)
print(s)
assert x != y

# 4.索引值
s = "water"
assert s[3] == "e"
assert s[-1] == "r"  # -1代表最后一个
assert s[:3] == "wat"  # 从左边数三个值
assert s[4] == s[-1]
# print(s[5])  # 会报错
# 或者 会把错误信息输出
try:
    s[5]
except IndexError as e:
    print(e)

# 5.返回值
s = "hello"
u = s.upper()
print(u)
print(s)  # 字符串是不可修改的

t = "name:{},age:{}"
print(t)
t1 = t.format("Jack", 21)
print(t1)


# 验证属性
# 1.对数学运算符 (+、-、*、/、//、%、@) 有没有支持
s1 = "abc"
s2 = "def"
s = s1 + s2
assert s == "abcdef"
print(s1 + s2)

try:
    print(s2 - s1)
except TypeError as e:
    print(e)

s = "$&"
s = s * 20
print(s)

s = "zzz"
print(s)
try:
    s = s / 4
except TypeError as e:
    print(e)

# 2.如何判断相等 (==)
assert s == "zzz"

# 3.对于比较运算符 (>、<、>=、<=) 有没有支持
print("abc" > "ABC")  # 代码位靠前就小，靠后就大  ascii-code.com
print("123" > "abc")
print("book" < "box")  # 先比较第一个字符，第一个代码位靠前整个就大

# 4.什么值被当作 True，什么值被当作 False
assert "book"  # 不报错，当作ture
# assert ""  # 会报错，当作false,只要字符串不为0，都会当作true

# 5.是否可迭代 (iterable)，如何做迭代 (for 循环)
s = "book"
print(iter(s))  # 如果不报错，是可迭代的
for c in s:
    print(c)

# 7.是否支持返回长度 (len)
print(len(s))

# 8.是否 (如何) 支持索引操作 (subscription) ([] 运算符)
s = "book"
assert s[1:3]  # 1是包含的，3是不包含的，结果是oo
breakpoint()

# 9.拥有哪些常用方法 (method) 可供调用 (() 运算符)  #import wat  wat /s   wat /s.  p s endswith('why')输出为TURE
s = "the book of why water you thoo nooo"
print(s.capitalize())  # 大写第一个字母
print(s)
print(s.count("oo") == 3)  # 用于统计某个元素在序列
print("abc123".isalnum())  # 判断字符串是否只包含字母和数字（不含空格、符号等）
print("abc_123".isalnum())
print(
    "abc123".isidentifier()
)  # 判断字符串是否符合 Python 变量名、函数名、类名等标识符的命名规则
print("123abc".isidentifier())


q = ["rose", "jacK", "kim"]
print(":".join(q))  # 连接字符串

# split 断开
s = "rose:jack:kim"
print(s.split(":"))

assert s.partition(":") == ("rose", ":", "jack:kim")

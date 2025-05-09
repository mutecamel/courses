# 通过字面值获得：
print("通过字面值获得：")
s = "hello"
print(s)
assert type(s) is str

# try f-string
x = "Blaze"
s = f"name:{x}"
print(s)

# 制表符
s = "a\tb"
print(s)

# 换行符
s = "aaa\nbbb"
print(s)

# 三引号允许字符串跨越多行
# 且保留格式：字符串中的换行、缩进、空格都会原样输出
s = """xyz
abc
    eee
aaa"""
print(s)


# 通过初始化获得：
print("通过初始化获得：")
s = str()  # 空字符串
print(s)

s = str([5, 8, 2])
print(s)
assert str([5, 8, 2]) == "[5, 8, 2]"
assert str(1.1 + 2.2) != "3.3"  # 二进制，不等


# 通过运算值获得：
print("通过运算值获得：")
s = "="
x = id(s)
s = s * 20  # 此时s指向的对象内存地址变化了
y = id(s)
print(s)
assert x != y


# 通过提取值获得：
print("通过提取值获得：")
s = "hello"
assert s[3] == "l"
assert s[:3] == "hel"
print(s[-1])
try:
    s[5]
except IndexError as e:
    print(e)


# 通过返回值获得：
print("通过返回值获得：")
s = "hello"
u = s.upper()
print(u)
print(s)

t = "name:{},age:{}"
print(t)
T = t.format("Blaze", 21)  # 并没有修改t
print(T)


# 其他属性和操作示例
print("其他属性和操作示例:")

# 1. 数学运算符
# 支持 + (拼接) 和 * (重复)
s1 = "Hello"
s2 = "World"
print(s1 + s2)
print(s1 * 3)
# 不支持 - / // % ** @

# 2. 比较运算
print("abc" == "abc")
print("abc" != "ABC")
print("apple" < "banana")  # 字典序（排在前的小）
print("Cat" < "cat")  # 基于ASCII

# 3. 布尔值
# 空字符串为False，非空为True
print(bool(""))  # False
print(bool(" "))  # True
print(bool("0"))  # True

# 4. 可迭代性
# 可用for循环遍历
s = "book"
print(iter(s))

for c in s:
    print(c)


# 5. 长度和索引
# 支持len()和下标访问
s = "Python"
print(len(s))  # 6
print(s[0])  # P
print(s[-1])  # n
print(s[1:4])  # yth

# 6. 常用方法(可以用wat检视)
# 大小写转换
print("Hello".lower())  # hello
print("hello".upper())  # HELLO

# 去空格
print("  hi  ".strip())  # hi

# 替换
print("hello".replace("l", "L"))  # heLLo

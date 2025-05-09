# 字面值
print("字面值")
s = "university"
print(s)
print(isinstance(s, str))
print(type(s))
assert type(s) is str
assert isinstance(s, str)
print("good")

print("f-string")
x = "Tom"
s = f"name: {x}"
print(s)

s = "a\tb"
print("TAB", s)

s = "abc\nxyz"
print("new words", s)

s = """xyz
aaa
 bbb
   ccc"""
print(s)

# 初始化
print("初始化")
s = str()
print(s)
s = str([5, 8, 2])
print(s, type(s))

# 运算值
assert str([5, 8, 2]) == "[5, 8, 2]"
assert str(1.1 + 2.2) != "3.3"


s = "abc"
s1 = s * 5
print(s1)


# 索引值
s = "hello world"
assert s[-1] == "d"
assert s[5] == " "  # 注意索引值字面值的第一位应该是第0个，最后一个为-1
assert s[0:5] == "hello"  # [:5][0:5]从左数第五个，所以不包含空格
try:
    s[11]
except IndexError:
    print("error")

# 返回值
a = "hello python"
b = a.upper()
print(b)

a = "ABC"
b = a.lower()
print(b)

t = "fruit:{},price{}"
t1 = t.format("apple", 2)
print(t1)

# 对数学运算符是否支持
s1 = "abc"
s2 = "xyz"
s = s1 + s2
print(s)
print(s2 + s1)  # 字符串之间不支持-，/，*等运算符，但字符串和数字之间支持

try:
    print(s1 - s2)
except TypeError as e:
    print(e)

# 判断相等
s = "aaaa"
try:
    s = s / 2
except TypeError as e:
    print(e)
assert s == "aaaa"

# 对比较运算符是否支持
print("abc" > "ABC")
print("123" > "abc")
print({1, 2, 3, 4} > {2, 3})
print({1, 2, 3} > {4})

# 是否可迭代
s = "book"
print(iter(s))
for c in s:
    print(c)

# 返回长度
s = "helloworld"
print(len(s))
print(s[2:5])
# 索引操作
s = "book"
assert s[1:3] == "oo"

s = "hello world hello python"
print(s.capitalize())  # 仅第一个单词首字母大写
print(s.title())  # 每个单词首字母大写
print(s.upper())  # 每个字母大写
print(s.count("h"))
print("abc123".isalnum())  # 字母+数字组合
print("abc_123".isalnum())
print("abc123".isidentifier())
print("abc_123".isidentifier())
print("abc-123".isidentifier())
print("123abc".isidentifier())

q = ["apple", "peach", "berry"]
print(":".join(q))  # 添加分隔符

q = "apple:peach:berry"
print(q.split(":"))  # 去除分隔符
assert q.partition(":") == ("apple", ":", "peach:berry")

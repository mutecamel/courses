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
print("TAB", s)

s = "aaa\nbbb"
print("New Line", s)

# raw-string, translate, multi-line

s = """xyz
abc
  eee
aaa
"""
print(s)


print("初始化")
s = str()
print(s)
s = str([5, 8, 2])
print(s)

assert str([5, 8, 2]) == "[5, 8, 2]"
assert str(1.1 + 2.2) != "3.3"

s = "="
x = id(s)
s = s * 20
y = id(s)
print(s)
assert x != y

s = "hello"
assert s[3] == "l"
assert s[-1] == "o"
assert s[:3] == "hel"
assert s[4] == s[-1]
try:
    s[5]
except IndexError as e:
    print(e)

s = "hello"
u = s.upper()
print(u)
print(s)

t = "name:{},age {}"
print(t)
t1 = t.format("Jack", 21)
print(t1)

s1 = "abc"
s2 = "ghi"
s = s1 + s2
assert s == "abcghi"
print(s1 + s2)

try:
    print(s2 - s1)
except TypeError as e:
    print(e)

s = "=*="
s = s * 10
print(s)

s = "aaaa"
try:
    s = s / 2
except TypeError as e:
    print(e)

assert s == "aaaa"

print("abc" > "ABC")
print("123" > "abc")
print("9" > ".")
print("9" < ":")
print("book" < "box")
print("book" < "{")

s = "book"
print(iter(s))

for c in s:
    print(c)

print(len(s))

s = "book"
assert s[1:3] == "oo"
# 1是包含的，3是不包含的，1到3是2个距离，所以是2个字母
breakpoint

s = "the book of why"
print(s.capitalize())
print(s)

s = "the book of why took noooo"
print(s.count("o"))
print(s.count("oo"))


# 检查字符串是否以指定后缀结尾
text = "Hello, world!"
print(text.endswith("world!"))  # 输出: True
print(text.endswith("Hello"))  # 输出: False
# 使用元组检查多个后缀
print(text.endswith(("world!", "Python")))  # 输出: True


str_example = "Hello, World!"
print(str_example.index("World"))
# 输出 7，因为 "World" 从原字符串的第 7 个位置开始（索引从 0 计数）

# 包含字母和数字的字符串
string1 = "abc123"
print(string1.isalnum())  # 输出: True
# 包含特殊字符的字符串
string2 = "abc@123"
print(string2.isalnum())  # 输出: False
# 空字符串
string3 = ""
print(string3.isalnum())  # 输出: False

print("abc123".isalnum())
print("abc123 ".isalnum())
print("abc123".isidentifier())
print("123abc".isidentifier())
print("abc_123".isidentifier())


# 使用逗号作为分隔符连接列表元素
my_list = ["apple", "banana", "cherry"]
result = ", ".join(my_list)
print(result)
# 输出: apple, banana, cherry
# 使用空字符串连接元组元素
my_tuple = ("Hello", "World")
result = "".join(my_tuple)
print(result)
# 输出: HelloWorld


# 移除首尾空白字符
text1 = "   Hello, World!   "
print(text1.strip())
# 移除开头的空白字符
print(text1.lstrip())
# 移除结尾的空白字符
print(text1.rstrip())
# 移除指定字符
text2 = "---Hello, World!---"
print(text2.strip("-"))

# 使用空格作为分隔符分割字符串
text = "Hello World Python"
result = text.split()
print(result)
# 使用逗号作为分隔符分割字符串
text = "apple,banana,cherry"
result = text.split(",")
print(result)
# 指定最大分割次数
text = "apple,banana,cherry"
result = text.split(",", 1)
print(result)

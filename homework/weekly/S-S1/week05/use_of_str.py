print("字面值")
s = "sport"
print(isinstance(s, str))
assert type(s) is str


print("f-string")
y = "baseball"
s = f"name:{y}"
print(s)

s = "a\tb"
print("TAB", s)

s = "a111\nb111"
print("22222", s)

s = """111222333
aaabbbccc
  444
333333
"""
print(s)


print("初始化")
s = str()
print(s)
s = str([1, 2, 3])
print(s)
assert str([1, 2, 3]) == "[1, 2, 3]"
assert str(1.1 + 2.2) != "3.3"

print("运算值")
s = "="
x = id(s)
s = s * 20
y = id(s)
print(s)
assert x != y

print("索引值")
s = "sport"
assert s[2] == "o"
assert s[-1] == "t"
assert s[:3] == "spo"
assert s[4] == s[-1]
try:
    s[5]
except IndexError as e:
    print(e)


print("返回值")
s = "sport"
x = s.upper()
print(x)

y = "name:{},age{}"
print(y)
yy = y.format("hahah", 66)
print(yy)


s = "abc"
ss = "222"
sss = s + ss
assert sss == "abc222"
print(sss + ss)

try:
    print(s - sss)
except TypeError as aaaaa:
    print(aaaaa)

a = "===*==="
a = a * 6
print(a)


a = "zzzzz"
try:
    a1 = a / 3
except TypeError as c:
    print(c)

assert a == "zzzzz"

print("比较大小")
print("aaa" > "bbb")
print("abc" > "ABC")
print("!" < "1")
print("?" > ":")
print("+1" < ":a")
print("111" < "22a")


print("是和否")
assert "sport"
assert not ""


print("迭代")
a = "sport"
print(iter(a))

for b in a:
    print(b)

print("长度")
print(len(a))

print("索引操作")
a = "sport"
assert a[0:4] == "spor"

a = "who are you"
print(a.capitalize())
print(a)
print(a.count("o") == 2)
print("aaa111".isalnum())
print("aaa!!111".isalnum())

print("aaa111".isidentifier())
print("222aaa111".isidentifier())
print("aaa-111".isidentifier())
print("aaa_111".isidentifier())

a = ["aaa", "bbb", "ccc"]
print(":".join(a))
p = "aaa:bbb:ccc"
print(p.split(":"))

print("移除内容")
text = "  Hello, World!  "
stripped_text = text.strip()
print(stripped_text)

text = "---Hello, World!---"
stripped_text = text.strip("-")
print(stripped_text)

text = "***Hello, World!!!***"
stripped_text = text.strip("*!")
print(stripped_text)

p = "aaa:bbb:ccc"
assert p.partition(":") == ("aaa", ":", "bbb:ccc")

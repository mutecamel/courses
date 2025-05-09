"""a = "hello"
b = "hello"
x = id(a)
print(x)
y = id(b)
print(y)"""  # 字符的id是一样的 每次运行都会生成新的id

"""
a = [3, 6]
b = [3, 6]
x = id(a)
print(x)
y = id(b)
a[0] = 8
print(a)
print(b)
print(id(a))  # 与上面的x一致吗 是的
print(id(b))  # 与上面的y一致吗 是的
print(type(a))
print(isinstance(a, str))  # 判断a是不是字符串 结果不是
print(isinstance(a, list))  # 判断a是不是列表 结果是
print(isinstance(a, (str, list)))  # 判断a的类型是不是二者之一
print("dir(a):", dir(a))
try:
    assert isinstance(a, str)
except AssertionError:
    print("type error")
    breakpoint()
print("hello caoji")"""

"""
print("字面值")
c = "caoji"
print(isinstance(c, str))
assert type(c) is str

print("f-string")
l = "ljj"
sg = f"name:{l}"
print(sg)


z = "k\to"  # TAB能保证k和o之间有三个空格
print("TAB", z)

i = "eco\npb"
print("NEW Line", i)"""

a = """qwer
adsw
  eco
you
"""
"""   print(a)

print("初始化")
b = str()
print(b)

b = str([3, 6, 0])
print(b)

assert str([3, 6, 0]) == "[3, 6, 0]"
assert str(3 - 1) == "2"
#  assert str(1.1 + 2.2) == "3.3" # 因为二进制中1.1＋2.2不等于3.3 会报错
assert str() == ""

c = "+"
c = c * 10
d = "-"
d = d * 5
print(c, d)

e = "maidong"
assert e[5] == "n"  # 从左开始的第六个字母，5+1
assert e[1] == "a"
assert e[-1] == "g"  # 从右开始的第一个字母
assert e[-2] == "n"  # 从右开始的第二个字母
assert e[:3] == "mai"  # 从左开始的三个字母

try:
    e[7]
except IndexError as g:
    print(g)

h = "cup"
i = h.upper()  # 返回值，小写变大写
print(i)
print(h)

t = "name:{}, weight{}"
print(t)
t1 = t.format("caoji", 170)  # 字符串不可被修改，只是调用了原来的字符串并对其进行了修改
print(t1)

w = "wo"
y = "you"
print(w + y)
assert (w + y) == "woyou"

try:
    print(w - y)
except TypeError as a:
    print(a)

a = "-+-=-+-"
a = a * 10
print(a)"""

a = "cao"
b = "CAO"
print(a > b)
print("abc" > "Abc")  # 字符串的大小与代码位有关
print("123" > "234")
print("9" > ".")
print("book" < "c")

assert "cao"  # 只要字符串的长度不是0，都是true
#  assert ""

a = "caoji"
print(iter(a))

for c in a:
    print(c)

print(len(a))

assert a[2:4] == "oj"
# breakpoint()
a = "cao ji zhen shuai book whoo zoo tooo"
print(a.capitalize())
print(a)
print(a.count("oo"))

print("fanzekai23".isalnum())
print("fanzekai 23".isalnum())  # 检验是否只有字母与数字
print("fzk231".isidentifier())  # 数字开头不能作为标识符
print("231fzk".isidentifier())

b = ["cj", "lyj", "ljj", "fzk"]
print(":".join(b))

c = "cj:lyj:ljj:fzk"
print(c.split(":"))
print(c.partition(":"))

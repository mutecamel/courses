##字面值相关
print("武汉攻略")
a = "walk street"
print(a)
print(isinstance(a, str))
assert type(a) is str

print("f-string")
x = "江汉步行街"
b = f"site: {x}"
print(b)

s = "武汉大学\t东湖"
print("TAB", s)

s = "武汉大学\n东湖"
print("New line", s)
# raw-string, translate, multi-line
# """表示换行
s = """wuhan university
west lake
"""
print(s)

##初始化，任何的对象都可以放在str()里，然后print
s = str([0, 5, 2, 6])
print(s)
assert str([0, 5, 2, 6]) == "[0, 5, 2, 6]"  ##初始化和字面值得到的字符串是一样的

##运算值,注意运算之后的id地址会改变
s = 20
x = id(s)
s = 20 * 5
y = id(s)
print(s)
assert x != y

##索引值，索引操作之后产生一个新对象，提取会从0开始,:5表示从左边开始连续的三个
s = "seventeen"
assert s[4] == "n"
assert s[-1] == "n"
assert s[:5] == "seven"
##只显示报错原因但是不报错
try:
    s[9]
except IndexError as e:
    print(e)

###返回值
s = "seventeen"
u = s.upper()  ##只是返回大写的实例，但是不修改原本的字符串，在Python中字符串不能被修改
print(u)
t = "member:{}, birth year:{}"
t1 = t.format("scoups", 1996)
print(t1)

##字符串可以用+，*但是不可以用-，÷
s = "bbbb"
s = s + "cccc"
print(s)
print(s * 5)
s = "bbbb"
try:
    print(s - "bb")
except TypeError as e:
    print(e)
try:
    print(s / 2)
except TypeError as e:
    print(e)
assert s == "bbbb"  ##判断字符串是否相等

##字符的排列规则：ASCII Table位置靠前就代表比较小；字符串的大小比较：字典序
print("seventeen" > "SEVENTEEN")
print("1" > ".")
print("@@" < "::")
print("seventeen" < "kpop")
print("你好" > "hello")
##字符串是否可以迭代循环用iter
s = "seven"
print(iter(s))
for c in s:  ##结束了自动绕过不算异常
    print(c)

print(len(s))  ##lne字符串的长度
assert s[1:4] == "eve"  ##索引操作包含1但不包含4

##常用可调用运算符
s = "seventeen right here"

print(s.capitalize())
print(s.count("e") == 6)  ##此处的6不是字符串而是数值
print(s.index("e") == 1)  ##第一个e出现的位置，还是从0开始数
s = ["scoups", "DK", "joshua"]
print(":".join(s))
s = "a!b!c"
print(s.split("!"))  ##根据！将字符串s分开

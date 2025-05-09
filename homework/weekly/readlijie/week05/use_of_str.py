print("字面值")
s = "library"
print(s)
print(isinstance(s, str))
assert type(s) is str
m = [2, 4]
print(m)
print(isinstance(m, list))

print("f-string")  # 字面值
x = "cat"
s = f"name: {x}"
print(s)

print("f-string")  # 字面值
x = "fish, rice, vegetable"
s = f"food: {x}"
print(s)  #  food: fish, rice, vegetable

print("f-string")  # 字面值
x = "111, 2573, 89796, abc"
s = f"number: {x}"
print(s)  #   number: 111, 2573, 89796, abc

print("f-string")
x = "meet"
s = f"brunch: {x}"
print(s)

s = "a\tb"
print("TAB", s)  #   TAB a   b

s = "abc\tbcd"
print("TAB", s)  #   TAB abc bcd

s = "aaabbccdbdbjcdaa\nbbbbbbbbnsbiucbidusbcidbb"
print("New Line", s)  # New Line aaabbccdbdbjcdaa回车bbbbbbbbnsbiucbidusbcidbb

s = "aaab16575cdaa\nbbbbi123?.,.,.,/dbb"
print("New Line", s)

s = """xyzxnsiucb
a   bcbswigi
  eeecnjck
        xxxxxbidci
aaa
"""
print(s)


print("初始化")  # 初始化
s = str()
print(s)

s = str([2, 4, 5, 6, 9999999999])
print(s)

assert str([2, 4, 5, 6, 9999999999]) == "[2, 4, 5, 6, 9999999999]"
assert str([1.1 + 2.2]) != "3.3"

assert str() == ""

s = "11anc11"  # 运算符
x = id(s)
s = s * 21
y = id(s)
print(s)
assert x != y

m = "byebyebyebye"
assert m[1] == "y"  # 索引从0开始，我的第一位是y，注意注意！
assert m[-1] == "e"  # -1是最后一位
assert m[-6] == "b"
assert m[:3] == "bye"
assert m[6] == m[-3]
try:
    m[100]
except IndexError as e:
    print(e)

s = "emmmmmo"  # upper返回值
u = s.upper()
print(u)
print(s)

t = "hobby: {}, age {}"  #  t是字符串，不可修改 （字符串类型） ； format返回值
print(t)
t1 = t.format("eat", 18)  # 是字符串实例 具体字符串
print(t1)

t = "food: {}, sex: {}, school: {}, language: {}"
print(t)
t1 = t.format("hamburger", "man", "cueb", "english")  # 是字符串实例 具体字符串
print(t1)  # food: hamburger, sex: man, school: cueb, language: english

s1 = "xyz"
s2 = "zzz"
s3 = "123"
s4 = "ji/..,"
s = s1 + s2 + s3 + s4
assert s == "xyzzzz123ji/..,"
print(s2 + s1 + s3 + s4)  # 字符串不能相减
print(s1 + s3 + s2 + s4)  # xyz123zzzji/..,

try:
    print(s1 - s2 - s3)
except TypeError as e:
    print(e)

s = "why=-=-="
s = s * 12
print(s)

s = "hihihihahaha"
y = "mmmmmnnnn"
s = s * (len(y) * 2)
print(s)

s = "hihihihahaha"
y = "mmmmmnnnn"
s = (s + y) * 2
print(s)  # hihihihahahammmmmnnnnhihihihahahammmmmnnnn
assert s == "hihihihahahammmmmnnnnhihihihahahammmmmnnnn"

s = "5"
m = "8"
print(s + m)  # 输出: 58  ；不支持减法，乘法

s = "aaaa"
try:
    s = s / 2
except TypeError as e:
    print(e)

assert s == "aaaa"  # 判断相等  两个字符串一模一样就是相当的

print("abc" > "ABC")  # 比较运算符 TRUE  字符有代码位
print("abcdfff" > "12567367")  # true
print("&^$^&" > "buou*&^79")  # false
print("9" < ":")  # true
print("book" < "?")  # false

assert "book"  # true
assert "buibui"  # 不是空的就不报错
assert not ""
assert "?.,,/"

s = "flower"
print(iter(s))  # 可迭代

for c in s:  # 做迭代
    print(c)

print(len(s))  # 返回长度

s = "flowersrosebloomy1123"
print(iter(s))  # 可迭代
for c in s:  # 做迭代
    print(c)
print(len(s))  # 返回长度


s = "reader"
assert s[1:5] == "eade"  # 索引    不算最后一个 5-1

s = "1y6656389"
assert s[2:8] == "665638"

s = "the emo of day he she heeeeeee"
print(s.capitalize())  # 第一个字母大写
print(s)
print(s.count("he") == 4)  # true    不重复查找

print("abc25235ARTHT".isalnum())  # true 字符串都是字母和数字
print("abc25235 ARTH？T".isalnum())  # false  混入空格和符号

print("abhcxv57r5".isidentifier())  # true   作为变量名标志符 数字开头不可以
print("1abhcxv57r5".isidentifier())  # false

q = ["rose", "flower", "black", "red"]
print(":".join(q))  # rose:flower:black:red
s = "rose:flower:red:egg"
print(s.split(":"))  # ['rose', 'flower', 'red', 'egg']
assert s.partition(":") == (
    "rose",
    ":",
    "flower:red:egg",
)  # 拆成三份， ： 左边 右边全部

q = ["rose", "flo111wer", "black", "2556"]
print(":".join(q))  # rose:flo111wer:black:2556
s = "rose:flo111wer:red:egg:456788:?//..."
print(s.split(":"))  # ['rose', 'flo111wer', 'red', 'egg', '456788', '?//...']
assert s.partition(":") == (
    "rose",
    ":",
    "flo111wer:red:egg:456788:?//...",
)

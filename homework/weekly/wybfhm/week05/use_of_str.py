print("字面值")
s = "university"
print(s)
print(isinstance(s, str))
assert type(s) is str

print("f -string")
x = "tom"
s = f"name: {x}"
print(s)

s = "a\tb"
print("TAB", s)

s = "abc\ndef"
print("great", s)

s = "nijint"
print(s)

s = "你吃饭了吗"
print(s)

print("初始化")
s = str()
print(s)
s = str([5, 8, 2])
print(s)
assert str([5, 8, 2]) == "[5, 8, 2]"
assert str(1.1 + 2.2) != "3.3"

assert str() == ""

s = "="
x = id(s)
s = s * 20
y = id(s)
print(s)
assert x != y

s = "hello"
assert s[3] == "l"
assert s[:3] == "hel"
assert s[4] == s[-1]

s = "hello"
u = s.upper()
print(u)
print(s)

s1 = "abc"
s2 = "def"
s = s1 + s2
assert s == "abcdef"
print(s1 + s2)

s = "aaaa"
assert s == "aaaa"

print("abc" > "ABC")
print("9" < ":")

s = "book"
print(iter(s))

for c in s:
    print(c)

print(len(s))

s = "the book of why kook nono"
print(s.capitalize())
print(s)
print(s.count("oo") == 3)

print("字面值")
s = "hi"
print(s)
print(isinstance(s, str))
assert type(s) is str

print("f-string")
x = "lucy"
s = f"name: {x}"
print(s)

s = "a\tb"
print("TAB", s)

s = "aa\nbb"
print("new", s)

print("初始化")
s = str()
print(s)
s = str([5, 8, 2])
print(s)

assert str([5, 8, 2]) == "[5, 8, 2]"
assert str(2.2 + 4.4) != "6.6"

assert str() == ""

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

t = "name: {},age {}"
print(t)
t1 = t.format("Tom", 22)
print(t1)

s1 = "abc"
s2 = "ghe"
s = s1 + s2
assert s == "abcghe"
print(s1 + s2)

try:
    print(s2 - s1)
except TypeError as e:
    print(e)

s = "=*="
s = s * 20
print(s)

s = "bbbb"
try:
    s = s / 2
except TypeError as e:
    print(e)

assert s == "bbbb"

print("ABC" > "abc")
print("abcd" > "123")
print("9" > ".")
print("9" > ":")
print("book" < "box")
print("book" < "{")

assert "book"
assert not ""

s = "book"
print(iter(s))

for c in s:
    print(c)

print(len(s))

s = "book"
assert s[1:3] == "oo"

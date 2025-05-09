print("字面值")
s = "university"
a = [33]
print(s)
print(a)
print(isinstance(s, str))
print(isinstance(a, str))
assert type(s) is str
print("f-string")
X = "5"
s = f"length:{X}"
print(s)

s = "a\tb"
print("TAB", s)

s = "aaa\nbbbb"
print("next line", s)
s = """abc
def
   xyz
     bbb
ccc"""
print(s)

print("初始化")
s = str()
print(s)
s = str([2, 3])
print(s)
assert str([2, 3]) == "[2, 3]"
assert str(1 + 2) == "3"

s = "2"
x = id(s)
s = s * 5
y = id(s)
print(s)
assert x != y

s = "world"
print(s[3])
assert s[3] == "l"
print(s[1])
print(s[:3])
assert s[:3] == "wor"
assert s[3] == s[-2]
try:
    s[5]
except IndexError as e:
    print(e)

s = "world"
u = s.upper()
print(s)
print(u)

t = "name: {}  age: {}"
t1 = t.format("cherry", 22)
print(t1)

s1 = "abc"
s2 = "xyz"
print(s2 + s1)
try:
    print(s2 - s1)
except TypeError as e:
    print(e)
print(s1 * 3)

s = "aaaa"
try:
    s = s / 2
except TypeError as e:
    print(e)
assert "abc" > "ABC"
print("123" > "a")
print("9" > ".")
try:
    "123" > "a"
except AssertionError as e:
    print(e)
print("zoo" > "zoom")

assert "yes"
assert not ""
s = "yes"
print(iter(s))

for c in s:
    print(c)

print(len(s))
try:
    print(len(4))
except TypeError as e:
    print(e)

s = "world"
assert s[1:4] == "orl"
print(s[1:4])
print(len(s[1:4]))

s = "hello world"
print(s.capitalize())
print(s)

print("adh892".isalnum())
print("sjh*2".isalnum())
print("sd34".isidentifier())
print("34sd".isidentifier())
print("sd*34".isidentifier())
print("sd+34".isidentifier())
print("sd^34".isidentifier())

q = ["a", "b", "c"]
print(";".join(q))
s = "2025-4-8"
print(s.split("-"))
assert s.partition("-") == ("2025", "-", "4-8")

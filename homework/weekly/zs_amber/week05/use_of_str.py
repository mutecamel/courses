"""
a = [2, 5]
b = [2, 5]
x = id(a)
print(x)
y = id(b)
print(y)
a[0] = 9
print(a)
print(b)
print(id(a))
print(id(b))
print(type(a))
print("isinstance(a,str):", isinstance(a, str))
print("isinstance(a,list):", isinstance(a, list))
print(isinstance(a, (str, list)))
print("dir(a):", dir(a))
try:
    assert isinstance(a, str)
except AssertionError:
    breakpoint()
    print("type error")
print("goodbye")
"""

print("字面值")
s = "iniversity"
print(s)
print(isinstance(s, str))
assert type(s) is str

print("f-string")
x = "Tom"
s = f"name:{x}"
print(s)

s = "a\tb"
print("Tab", s)

s = "aaa\nbbb"
print("NewLine", s)

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

s = "Hello"
assert s[3] == "l"
assert s[-1] == "o"
assert s[:3] == "Hel"
assert s[4] == s[-1]

s = "hello"
u = s.upper()
print(u)
print(s)

t = "name:{},age{}"
print(t)
t1 = t.format("Jack", 21)
print(t1)

s1 = "abc"
s2 = "ghi"
s = s1 + s2
assert s == "abcghi"
print(s2 + s1)

s = "book"
print(iter(s))

for c in s:
    print(c)

print(len(s))
s = "book"
assert s[1:3] == "oo"

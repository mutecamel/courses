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
print("new line", s)


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

assert str() == ""

c = "="
x = id(c)
c = c * 18
y = id(c)
print(c)
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

c = "sally"
u = c.upper()
print(u)
print(c)

c = "name: {}, age {}"
print(c)
c1 = c.format("jack", 21)
print(c1)

c1 = "abc"
c2 = "xyz"
c = c1 + c2
assert c == "abcxyz"
print(c1 + c2)

try:
    print(c1 - c2)
except TypeError as e:
    print(e)

c = "=*="
c = c * 10
print(c)

c = "aaaa"
try:
    c = c / 2
except TypeError as e:
    print(e)

assert c == "aaaa"

print("abc" > "ABC")
print("123" < "abcd")
print("9" > ".")
print("9" < ":")
print("book" < "box")
print("book" < "{")

assert "book"
assert not ""

c = "book"
print(iter(c))

for d in c:
    print(d)

    print(len(c))

c = "book"
assert c[1:3] == "oo"

s = "the book why took nooo"
print(s.capitalize())
print(s)
print(s.count("oo"))

print("abc123".isalnum())
print("abc123 ".isalnum())
print("abc123".isidentifier())
print("123abc".isidentifier())
print("abc_123".isidentifier())
print("abc-123".isidentifier())

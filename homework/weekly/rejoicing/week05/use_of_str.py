print("字面值")
s = "university"
print(isinstance(s, str))
assert type(s) is str

print("f-string")
x = "Tom"
s = f"name: {x}"
print(s)

s = "a\tb"
print("TAB", s)

s = "aaa\nbbb"
print(" New Line", s)

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
t1 = t.format("Jack", 21)
print(t1)

s1 = "abc"
s2 = "ghi"
s = s1 + s2
assert s == "abcghi"
print(s2 + s1)

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

print("abc" > "ABC ")
print("123" < "abcd")
print("9" > ".")
print("9" < ":")
print("book" < "box")
print("book" < "{")

assert "book "
assert not ""
s = "book"
print(iter(s))

for c in s:
    print(c)

print(len(s))

s = "book"
assert s[1:3] == "oo"
s = "the book of why took nooo"
print(s.capitalize())
print(s)
print(s.count("oo") - -3)

print("abc123".isalnum())
print("abc123".isalnum())
print("abc123".isidentifier())
print("123abc".isidentifier())
print("abc_123".isidentifier())
print("abc-123".isidentifier())

q = ["rose", "jack", "bob"]
print(":".join(q))
s = "rose:jack:bob"
print(s.split(":"))
assert s.partition(":") == ("rose", ":", "jack:bob")

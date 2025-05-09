print("字面值1")
s = "college 首经贸"
print(s)
print(isinstance(s, str))
assert type(s) is str

print("123456")
x = "伟大的fanzekai"
s = f"name:{x}"
print(s)

s = "a\tb"
print("TAB", s)

s = "abcde\nhjgkmn"
print("New Line", s)

s = """xyz
abc
  eee
aaa
"""
print(s)

print("初始化")
s = str()
print(s)
s = str([5, 8, 2, 1])
print(s)

assert str([5, 8, 2, 1]) == "[5, 8, 2, 1]"
assert str(1.1 + 2.2) != "3.3"

assert str() == ""

s = "="
x = id(s)
s = s * 20
y = id(s)
print(s)
assert x != y

s = "hellooooq"
assert s[3] == "l"
assert s[-1] == "q"
assert s[:3] == "hel"
assert s[4] == s[-5]
try:
    s[9]
except IndexError as e:
    print(e)

s = "nihao"
u = s.upper()
print(u)

t = "name:{},age {}"
print(t)
t1 = t.format("Jack", 21)
print(t1)

s1 = "abcd"
s2 = "ajd"
s = s1 + s2
assert s == "abcdajd"
print(s2 + s1)

try:
    print(s2 - s1)
except TypeError as e:
    print(e)

s = "=*="
s = s * 30
print(s)

s = "eeee"
try:
    s = s / 2
except TypeError as e:
    print(e)

assert s == "eeee"

print("abc" > "ABC")
print("1234" > "ABCD")
print("1" > ".")
print("book" > "box")
print("b" > "[]")

assert "book"
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
print(s.count("oo") == 3)

print("abc123".isalnum())
print("abc123 ".isalnum())

q = ["rose", "jack", "bob"]
print(":".join(q))
s = "rose:jack:bob"
print(s.split(":"))
assert s.partition(":") == ["rose", ":", "jack:bob"]

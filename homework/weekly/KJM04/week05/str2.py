print("字面值")
s = "university"
print(s)
print(isinstance(s, str))
assert type(s) is str

print("f_string")
x = "Tom"
s = f"name:{x}"
print(s)

s = "cue\tb"
print("TAB", s)

s = "cue\nb"
print("New Line", s)

s = """ccc
uuu
   eee
bbb
"""
print(s)

print("初始化")
s = str()
print(s)
s = str([5, 8, 2])
print(s)

assert str([5, 8, 2]) == "[5, 8, 2]"
assert str(1.1 + 2.2) != "3.3"


s = "="
x = id(s)
s = s * 20
y = id(s)
print(s)
assert x != y

s = "hello"
assert s[3] == "l"
assert s[-1] == "o"
assert s[4] == s[-1]
try:
    s[5]
except IndexError as e:
    print(e)

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

print("abc" > "ABC")
print("123" > "abcd")
print("book" > "box")

s = "book"
print(iter(s))

print(len(s))

s = "book"
assert s[1:3] == "oo"

s = "the book of why"
print(s.capitalize())
print(s)
print(s.count("oo") == 3)

print("abc123".isalnum())
print("abc_123".isalnum())
print("abc123".isidentifier())

q = ["rose", "jack", "bob"]
print(":".join(q))
s = "rose:jack:bob"
print(s.split(":"))
assert s.partition(":") == ("rose", ":", "jack:bob")

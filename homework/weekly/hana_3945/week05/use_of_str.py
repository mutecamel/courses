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
print("NEW LINE", s)

# raw-string, translate,multi-line
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

s = "="
x = id(s)
s = s * 20
y = id(s)
print(s)
assert x != y
s = "hello"
u = s.upper()
print(u)
print(s)

t = "name:{},age {}"
print(t)
t1 = t.format("Jack", 21)
print(t1)

s1 = "abc"
s2 = "ghi"
s = s1 + s2
assert s == "abcghi"
print(s2 + s1)


print("abc" > "ABC")
print("123" > "abcd")
print("book" < "box")
print("9" < ":")

assert "book"
s = "book"
print(iter(s))


for c in s:
    print(c)

print(len(s))
s = "the book of why"
print(s.capitalize())
print(s)

q = ["rose", "jack", "bob"]
# 使用正确的join方法调用
print(":".join(q))

s = "rose:jack:bob"
# 使用正确的split方法调用
print(s.split(":"))

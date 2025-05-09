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
print("New Line", s)


print("初始化")
s = str()
print(s)
s = str([5, 8, 2])
print(s)

assert str(1 + 2) == "3"

print("运算值")
s = "="
s = s * 20
print(s)

print("索引值")
s = "hello"
print(s[3])
assert s[3] == "l"
assert s[:3] == "hel"

print("返回值")
s = "hello"
s = s.upper()
print(s)

t = "name:{},age:{}"
print(t)
t1 = t.format("Jack", 21)
print(t1)

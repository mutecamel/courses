print("字面值")
a = "house"
print(a)
print(isinstance(a, str))
assert type(a) is str

print("f-string")
b = "man"
a = f"gender:{b}"
print(a)

a = "c\tc\tc"
print("TAB", a)

a = "ccc\nooo\nppp"
print("New Line", a)

print("初始化")
a = str()
print(a)
a = str([2, 3, 4])
print(a)

a = str()
print(a)
b = str([2, 3, 4])
print(id(a))
print(id(b))

assert str([3, 4, 5]) == "[3, 4, 5]"
assert str(1 + 2) == "3"
assert str(2.1 + 2.1) == "4.2"
print(2.1 + 2.1)
assert str(1.1 + 2.1) == "3.2"


print("运算值")
a = "+"
x = id(a)
b = a * 10
y = id(b)
print(b)
assert x != y

print("索引值")
s = "wonderful"
assert s[4] == "e"
assert s[-1] == "l"
assert s[:4] == "wond"
assert s[8] == s[-1]

print("返回值")
a = "goodbye"
b = a.upper()
print(a)
print(b)

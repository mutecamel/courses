print("f-string")
a = "dokyeom"
b = f"name: {a}"
print(b)

c = "9\t10"
print("TAB", c)
d = "999\n101010"
print("NEW LINE", d)


# 普通字符串
normal_string = "第一行\n第二行"
print(normal_string)

# 原始字符串
raw_string = r"第一行\n第二行"
print(raw_string)

# assert str(9.9 + 10.10) == "20"
assert str(9.9 + 10.10) != "20"

a = "*"
b = "a" * 9
print(b)

a = "dokyeom"
assert a[0] == "d"
assert a[-1] == "m"
assert a[:4] == "doky"
assert a[6] == a[-1]

t = "name: {}, age {}"
print(t)
e = t.format("dokyeom", 28)
print(e)

s1 = "dokyeom"
s2 = "mingyu"
s = s1 + s2
assert s == "dokyeommingyu"
print(s2 + s1)

print("dokyeom" > "mingyu")
print("abc" > "ABC")
assert "DOKYEOM"
# assert ""

s = "dokyeom"
print(iter(s))
for c in s:
    print(c)

a = "dokyeom"
assert a[1:3] == "ok"

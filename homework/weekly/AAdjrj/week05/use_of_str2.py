print("字面值")
s = "university"
print(s)
print(isinstance(s, str))
assert type(s) is str


print("f-string")
x = "tom"
s = f"name:{x}"
print(s)

s = "a\tb"
print("TAB", s)

s = "aaa\nbbb"
print("New Line", s)


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
print("9" < ":")
print("book" < "{")

assert "book"
assert not ""

s = "book"
print(iter(s))

# breakpoint()
for c in s:
    print(c)

print(len(s))

s = "book"
assert s[1:3] == "oo"  # 1包含，3不包含
# breakpoint()

s = "the book of why took nooo"
print(s.capitalize())
print(s)
print(s.count("oo") == 3)
# breakpoint()

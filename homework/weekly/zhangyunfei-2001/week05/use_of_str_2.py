print("abc" > "ABC")
print("123" > "abcd")
assert "book"

s = "book"
print(iter(s))
for c in s:
    print(c)

print(len(s))
s = "book"
assert s[1:3] == "oo"


q = ["rose", "jack", "bob"]
print(":".join(q))

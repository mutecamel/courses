a1 = "asd"
a2 = "fgh"
a = a1 + a2
assert a == "asdfgh"
print(a2 + a1)

try:
    print(a1 - a2)
except TypeError as e:
    print(e)

a = "+*+"
s = a * 5
print(s)

a = "asd"
b = "fgh"
try:
    s = a * b
except TypeError as e:
    print(e)

s = "dfh"
try:
    s = s / 6
except TypeError as e:
    print(e)
assert s == "dfh"

print("dfg" > "DFG")
print("345" > "asd")
print("6" > ".")
print("god" > "good")
print("bus" > "[]")

assert "apple"
assert not ""

a = "apple"
print(iter(a))

for c in a:
    print(c)

print(len(a))

a = "apple"
assert a[2:4] == "pl"

s = "i miss you"
print(s.capitalize())
print(s)

print("789hui".isalnum())
print("789_hui".isalnum())
str1 = "valid_identifier"
print(str1.isidentifier())
str2 = "123invalid"
print(str2.isidentifier())


numbers = ("1", "2", "3", "4")
result = ", ".join(numbers)
print(result)

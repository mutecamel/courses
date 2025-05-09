s = {2, 4, 8}
print(s)
print(type(s))

try:
    s = {2, [4], 8}
except TypeError as e:
    print(e)

q = [1, 2, 1, 2, 6, 1]
print(q)
s = set(q)
print(s)

s = {6, 2, 1, 2, 2, 1}
print(s)
print(2 in s)
print(3 in s)

s2 = {4, 1, 2}
print(s | s2)
print(s & s2)
print(s ^ s2)
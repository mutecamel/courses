s = {1, 2, 3}
print(type(s))

try:
    s = {1, [4], 7}
except TypeError as e:
    print(e)


q = [1, 2, 1, 2, 4, 5, 6]
print(q)
s = set(q)
print(s)

print(3 in s)  ##判断

s1 = {1, 2, 3}
print(s | s1)
print(s & s1)

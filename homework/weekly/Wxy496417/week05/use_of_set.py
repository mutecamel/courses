s = {1, 4, 7}
print(s)
print(type(s))

try:
    s = {1, {4}, 7}
except TypeError as e:
    print(e)

s = {1, (4, 3), 7}
print(s)
print(type(s))

q = [1, 2, 1, 2, 5, 1]
print(q)
s = set(q)
print(s)

s = {5, 2, 1, 2, 1, 1}
print(s)
print(2 in s)
print(3 in s)

s1 = {3, 2, 1}
print(s | s1)
print(s & s1)
print(s ^ s1)

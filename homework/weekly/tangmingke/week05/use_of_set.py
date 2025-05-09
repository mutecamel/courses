s = {1, 4, 7}
print(s)
print(type(s))

try:
    s = {1, 4, 7}
except TypeError as e:
    print(e)

q = [1, 2, 1, 2, 5, 1]
print(q)
s = set(q)
print(s)

s = [5, 2, 1, 2, 2, 1]
print(s)
print(2 in s)
print(3 in s)

s2 = {3, 2, 3}
print(s | s2)
print(s & s2)
print(s ^ s2)

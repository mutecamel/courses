q = {1, 3, 4}
print(q)
print(type(q))

try:
    q = {1, {3}, 2}
except TypeError as e:
    print(e)

d = [2, 34, 6, 5]
print(d)
s = set(q)
print(s)

s = {
    3,
    4,
    5,
    6,
    7,
}
print(s)
print(3 in s)
print(2 in s)

s2 = {3, 3, 2}
print(s | s2)
print(s & s2)

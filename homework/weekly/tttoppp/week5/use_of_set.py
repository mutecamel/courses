s = {1, 2, 3}
print(type(s))

try:
    s = {1, [2], 'm'}
except TypeError as e:
    print(e)

m = {1, 1, 3, 2, 1}
print(m)
print(1 in m)
print(5 in m)

n = {2, 5, 1}
print(m | n)
print(m & n)
print(m ^ n)

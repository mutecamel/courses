print("字面值")
s = {1, 9, 0}
print(s)
print(type(s))

try:
    s = {1, [9], 0}
except TypeError as e:
    print(e)

print("初始化")
a = [2, 3, 4, 4, 3, 5]
print(a)
s = set(a)
print(s)

s = {2, 3, 4, 4, 3, 5}
print(s)
print(2 in s)
print(9 in s)

s2 = {1, 2, 3}
print(s | s2)
print(s & s2)
print(s ^ s2)

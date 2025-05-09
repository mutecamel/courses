a = (1, "abc", 3.1415926, "fzk")  # 与list类似
print(a)
print(type(a))

print(a[0])
print(a[1])
print(a[2])

# a[0] = 2

b = {}
b["asd"] = 2
b[4] = 50
d = [1, 2, 3]
try:
    b[d] = 11
except TypeError as e:
    print(e)


a = (1, 7)
b[a] = 55

print(b)
print(b[1, 7])

l = [1, 5, "abc"]
print(l)

print(l[0])
print(l[-1][1])

a = [2, 5, 3]
b = [i**2 for i in a]
print(b)
b = [i**2 for i in a if i < 4]
print(b)

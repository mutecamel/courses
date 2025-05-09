l = ['a', 2, 2.2]
print(type(l))
print(l)

q = ['b', 3.5, 1]
print(l + q)
print(l[0])
print(l[1])
print(l[2])

try:
    print(l[3])
except IndexError as e:
    print(e)

m = [1, 2, 3]
n = [4, 5, 6]
print(m + n)
print(n + m)
print(m * 2)


print(m[-1])
print(m[-1],m[0])
print(l[0][0])

try:
    print(m - n)
except TypeError as e:
    print(e)

##对象不同
p = ['m', 2]
q = p * 2
p[0] = 'n'
print(p)
print(q)

p = ['m', 2]
q = [p] * 2
print(q)
p[0] = 'n'
print(q)

p = [1, 2, 3]
q = [i**3 for i in p]
print(q)

p = ['m', 'n']
q = [i+'m' for i in p]
print(q)

p = [1, 'm', 3]
q = [i+2 for i in p if type(i) != str]
print(q)

a = [1, 2, 3]
b = a.append(4)
print(b)
print(a)
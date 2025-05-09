t = ('q', 1.1, ['m', 2])
print(type(t))

print(t[2])

try:
   t[1] = 1
except TypeError as e:
   print(e)

print(t)

d = {}
d['a'] = 1
d[10] = 10
print(d)

try:
   d[Q] = 1
except NameError as e:
   print(e)

t = ('a', 1)
d[t] = 2
print(d)
print(d['a', 1])

t = 'm', 2.2, 1
print(t)
print(type(t))
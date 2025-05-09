a = {'a':2, 'b':3}
print(a)
print(type(a))

for i in a:
    print(i)
    print(a[i])
for b in a:
    print(a[b])

for i in a.values():
    print(i)

l = [i for i in a.items()]
print(l)

assert not {}

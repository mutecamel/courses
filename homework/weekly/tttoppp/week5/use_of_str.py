print('字面值')
a = 'TOP'
print(type(a))
print('isinstance(a, list):', isinstance(a, list))
print('isinstance(a, str):', isinstance(a, str))
assert type(a) is str

print('f-string')
b = f'my favorite singer:{a}'
print(b)

c = 'big\tbang'
print("TAB means 空格,", c)

d = 'bang\nbang\nbang'
print('New Line means 换行', d)

e = """1
2
3
4
 5
6
"""
print('""" means 原样保留', d)

print('初始化')
f = str()
print(f)
f = str('fafafa')
print(f)

assert str('fafafa') == 'fafafa'
assert str() == ''

g = '^'
h = '_'
m = '你生气啦？' + g + h + g
print(m)
n = (g + h + g) * 100
print(n)

i ='bang bang bang 123123'
print(i[4])
print(i[5])
print(i[15])
print(i[-1])
print(i[:11])

j = 'BIG BANG'
k = j.lower()
print(j)
print(k)

l = '年龄: {}, 身高: {}, 体重:{}'
print(l)
l1 = l.format(26, 188, 160)
print(l1)

m = '1'
n = '2'
o = m + n
print(o)
try:
    o = m - n
except TypeError as e:
    print(e)
try:
    o = m * n
except TypeError as e:
    print(e)
try:
    o = m * n
except TypeError as e:
    print(e)
try:
    o = m ** n
except TypeError as e:
    print(e)
try:
    o = m / n
except TypeError as e:
    print(e)
try:
    o = m // n
except TypeError as e:
    print(e)
try:
    o = m % n
except TypeError as e:
    print(e)
try:
    o = m @ n
except TypeError as e:
    print(e)

assert m == '1'

print('xyz' > 'XYZ')
print('6' > '5')
print('5+9' > '6+10')
print('A' > '@')
print('1234' < '1235' )
print('123456' >= '123456')

assert 'jiujiwudiguishi'
assert not ''

p = 'jiujiwudiguishi'
print(iter(p))

for q in p:
    print(q)

print(len('jiujiwudiguishi'))
assert p[5:9] == 'wudi'
print(p[5:9])
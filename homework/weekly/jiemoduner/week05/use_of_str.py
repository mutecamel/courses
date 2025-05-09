print('字面值')
s = 'university'
print(s)
print(isinstance(s,str))
assert type(s) is str

print('f-string')
x = 'Tom'
s = f'name: {x}'
print(s)

s = 'a\tb'
print('TAB',s)

print('初始化')
s = str()
print(s)
s = str([5,8,2])
print(s)

assert str(1.1 + 2.2) != '3.3'

assert str() == ''

s = '='
s = s * 20
print(s)

s = 'hello'
assert s[3] == 'l'
assert s[-1] == 'o'
assert s[:3] == 'hel'

s = 'hello'
u = s.upper()
print(u)
print(s)

s1 = 'abc'
s2 = 'ghi'
s = s1 + s2
assert s == 'abcghi'
print(s2 + s1)

s = '=*='
s = s * 10
print(s)

s = 'aaa'
try:
    s = s/2
except TypeError as e:
    print(e)

assert s == 'aaa'

print('abc' > 'ABC')
print('123' > 'abcd')


assert 'book'
assert not ''

s = 'book'
print(iter(s))

for c in s:
    print(c)

print(len(s))

s = 'book'
assert s[1:3] == "oo"

s = 'the book of why'
print(s.capitalize())
print(s)


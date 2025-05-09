print('字面值')
s = 'university'
print(s)
print(isinstance(s,str))
assert type(s) is str

print('f-string')
x = 'Tom'
s = f'name:{x}'
print(s)

s = 'a\tb'
print('TAB',s)

s = 'aaa\nbbb'
print('New Line',s)

print('初始化')
s = str()
print(s)
s = str([5,8,2])
print(s)

assert str([5, 8, 2]) == '[5, 8, 2]'


s = '='
s = s * 20
print(s)

s = 'hello'
assert s[3] == 'l'
assert s[-1] == 'o'

s = 'hello'
u = s.upper()
print(u)
print(s)

t = 'name: {},age {}'
print(t)
t1 = t.format('Jack',21)
print(t1)

print('abc' > 'ABC')
print('123' < 'abcd')
print('9' > '.')
print('book' < 'box')

assert 'book'
assert not ''

s = 'book'
print(iter(s))

for c in s:
    print(c)

print(len(s))

s = 'book'
assert s[1:3] == "oo"

s = 'the book of why  took nooo'
print(s.capitalize())
print(s)
print(s.count('oo') == 3)

print('abc123'.isalnum())
print('abc123 '.isalnum())
print('abc123'.isidentifier())
print('abc_123'.isidentifier()) 

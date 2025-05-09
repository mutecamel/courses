print ('字面值')
s = 'university'
print (s)
print(isinstance(s,str))
assert type(s) is str

print ('f-string')
x = "Tom"
s = f'name:{x}'
print (s)

s = 'a\tb'
print('TAB',s)

s = 'aaa\nbbb'
print ('NEW-line', s)

print('初始化')
s = str()
print(s)
s = str([2,5,8])
print (s)

assert str(1.1+2.2) != '3.3'

s = '='
u = s*10
print (u)

s='hello'
print(s[4])

s = 'hello'
u = s.upper()
print(u)


print('aaa'>'abc')

s ='book'
print(iter(s))

for c in s:
    print(c)

s = "Hello, World! "

print(s.upper())
print(s.lower())
print(s.find("or"))
print(s.replace("World", "China"))

text_with_spaces = "   Hello, World!   "
print(text_with_spaces.strip())
print( text_with_spaces.lstrip())
print(text_with_spaces.rstrip())

words = s.split()
print( words)
print(", ".join(words))
print( len(s))
print( s.startswith("Hello"))
print(s.endswith("ld!"))   


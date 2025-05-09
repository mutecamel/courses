print("字面值")
s = "Spring"
print(isinstance(s, str))
assert type(s) is str

print("f-string")
x = "Tom"
s = f"name:{x}"
print(s)

print("初始化")
s = str()
print(s)
s = str([1, 2, 3])
print(s)


print("索引值")
my_list = [10, 20, 30, 40, 50]
print(my_list[0])  # 输出 10
print(my_list[2])  # 输出 30

print("返回值")
s = "hello"
u = s.upper()
print(u)
print(s)

t = "name:{},age{}"
print(t)
t1 = t.format("张三", 18)
print(t1)

print("验证数学运算符是否支持")
s1 = 'abc'
s2 = 'ghi'
s = s1 + s2
assert s == 'abcghi'
print(s2 + s1)

try:
    print(s1 - s2)
except TypeError as e:
    print(e)

s = '=*='
s = s * 10
print(s)

print("如何判断是否相等")
a = [1, 2, 3]
b = [1, 2, 3]
assert a == b

print("对于比较运算符有没有支持")
print('$' > '%')
print('*' > '%')

print("True or False")
assert 'book'
assert not ''

print("是否可迭代")
s = 'smile'
print(iter(s))

for c in s:
    print(c)

print("是否支持返回长度")
print(len(s))

print("是否支持索引")
s = 'smile'
assert s[1:3] == "mi"
breakpoint()

s = 'Tokyo flash'
print(s.capitalize())
print(s)

a=[2,5]
b=[2,5]
x=id(a)
print(x)
y=id(b)
print(y)
a[0]=9
print(a)
print(b)
print (id(a))
print (id(b))
print(type(a))
print('isinstance(a,str):',isinstance(a,str))
print('isinstance(a,list):',isinstance(a,list))
print(isinstance(a,(str,float)))
try:
    assert isinstance(a,str)
except AssertionError:

 # 实例(字面值)
 v = "aaaa"
assert type(v) is str

print("f-string")
y1 = "honghong"
t1 = f"name: {y1}"
print(t1)

t = "c\td"  
print("TAB", t)

# 初始化
print("chushihua")
t = str()
print(t)
t = str([95588, 8888, 123])
print(t)

# 运算值
t = "-"
t = t * 20
print(t)

# 索引值
t = "banana"
assert t[2] == "n"  # python的字符串是从0开始计算
print(t[:4])

# 返回值
t = "tianqiyubao"
e = t.upper()
print(e)

# 运算符号
i = "wangzhan"
j = "8901"
print(i + j)

t = "###-###"
t = t * 9
print(t)

assert "bbbcd" > "BBBCD"
print("def" > "456")

t = "tianqiyubao"
for char in t:
    print(char)
print(len(t))

t = "xiyouji:baimawen:sunwukong"
print(t.split(":"))

breakpoint()

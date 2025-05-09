#for变量in被处理的数据
"""
name="itheima"
for x in name:
    print(x,end='')
"""
#练习题，找里面有几个字母A
"""
name="itheima is a brand of itcast"
i=0
for x in name:
    if x=="a":
        i+=1#循环结束后最后到下一步
print(f"被统计的字符中有{i}个a")
"""
"""
#range的语法
for x in range(10):
    print(x,end='')
print()
for x in range(5,10):
    print(x,end='')
print()
for x in range(5,100,4):
    print(x,end='')
"""
#练习题
"""
num=int(input("请输入一个100以内的数字:"))
i=0
for x in range(1,100):
    if x<=num:
        if x%2==0:
            i+=1
print(i)
x=1
for x in range(1,101):
    print(f"今天是向小美表白的第{x}天")
    for j in range(1,11):
        print(f"给小美的第{j}朵玫瑰花")
print(f"今天是表白的第{x}天，表白win")
"""
#for循环弄99乘法表
for i in range(1,10):
    for j in range(1,10):
        if j<=i:
            print(f"{j}*{i}={i*j}\t",end='')
    print()
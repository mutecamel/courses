#打开文件
f=open("D:/测试.txt","r",encoding='UTF-8')
print(type(f))
#读取文件-read（）
"""
print(f'读取十个字节的结果{f.read(10)}')
print(f'读取全部内容的结果{f.read()}')#会继续上一次剩下的
lines=f.readlines()#读取文件的全部行，封装到列表中
print(f'lines对象的类型是：{type(lines)}')
print(f'lines对象的内容是：{lines}')
"""
"""
#读取文件-readline()
line1=f.readline()
line2=f.readline()
line3=f.readline()
print(f"第一行的数据是：{line1}")
print(f"第二行的数据是：{line2}")
print(f"第三行的数据是：{line3}")

#for循环读取文件
for line in f:
    print(f"每一行数据是：{line}")

#文件的关闭
f.close()
"""
with open("D:/测试.txt","r",encoding='UTF-8') as f:
    for line in f:
        print(f"每一行的数据：{line}")
time.sleep(500000)

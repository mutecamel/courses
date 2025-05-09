#统计str长度，并且不用len函数
str1="itheima"
str2="itvast"
str3="python"
"""
#定义一个计数的变量
count=0
for i in str1:
    count+=1
print(f"str1{str1}的长度是：{count}")

count=0
for i in str2:
    count+=1
print(f"str2{str2}的长度是：{count}")

count=0
for i in str3:
    count+=1
print(f"str3{str3}的长度是：{count}")
"""
#可以用函数来优化
def my_len(data):
    count=0
    for i in data:
        count+=1
    print(f"字符串{data}的长度是{count}")
my_len(str1)
my_len(str2)
my_len(str3)




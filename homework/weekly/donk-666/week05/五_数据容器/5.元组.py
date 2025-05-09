#元组一旦定义便不可修改
#定义元组的字面量
#定义元组
t1=(1,"hello",True)
t2=()
t3=tuple()
print(f"t1的类型是：{type(t1)},内容是：{t1}")
print(f"t2的类型是：{type(t2)},内容是：{t2}")
print(f"t3的类型是：{type(t3)},内容是：{t3}")

t4=("hello",)

#嵌套的元组
t5=((1,2,3),(4,5,6))
print(f"t5的类型是：{type(t5)},内容是：{t5}")

#下表索引取出内容
num=t5[1][2]
print(f'从嵌套元组中取出的数据是：{num}')

"""
index()寻找某个数据，如果数据存在返回对应的下标，否则报错
count()统计某个数据在当前元组出现的次数
len(元组)统计元组的元素个数
"""

#元组的操作：index查找方法
t6=("传智教育","黑马程序员","python")
index=t6.index("黑马程序员")
print(f"在元组t6中查找黑马程序员，的下标是：{index}")

t7=("传智教育","黑马程序员","黑马程序员","黑马程序员","python")
num=t7.count("黑马程序员")
print(f"在元组t7中黑马程序员的数量有：{num}个")

t8=("传智教育","黑马程序员","黑马程序员","黑马程序员","python")
num=len(t8)
print(f"t8中的元素有：{num}个")

#元组的遍历：while
index=0
while index<len(t8):
    print(f"元组的元素有：{t8[index]}")
    index+=1
t8=("传智教育","黑马程序员","黑马程序员","黑马程序员","python")
for element in t8:
    print(f"2元素的元组有：{element}")
"""
元组的注意事项:
1.元组中的元素不可以修改
2.元组中的list内容可以修改
"""
t9=(1,2,["itheima","itvast"])
print(f"t9的内容是：{t9}")
t9[2][0]='黑马程序员'
t9[2][1]='传智教育'
print(f"t9的内容是：{t9}")

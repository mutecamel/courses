#列表，元组，字符串，均可以视为序列
#序列的语法：序列[启始下标:结束下标:步长]
my_list=[0,1,2,3,4,5,6]
result1=my_list[1:4]#步长默认为1
print(f"结果1是{result1}")

my_tuple=(0,1,2,3,4,5,6)
result2=my_tuple[:]
print(f"结果2是{result2}")

my_str="01234567"
result3=my_str[::2]
print(f"结果3是{result3}")

my_str="01234567"
result4=my_str[::-1]#等同于将序列反转
print(f"结果4是{result4}")

my_list=[0,1,2,3,4,5,6]
result5=my_list[3:1:-1]#步长默认为1
print(f"结果5是{result5}")

my_tuple=(0,1,2,3,4,5,6)
result6=my_tuple[::-2]
print(f"结果2是{result6}")


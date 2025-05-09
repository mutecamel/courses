my_str="itheima and itcast"
#通过下标索引取值
value=my_str[2]
value2=my_str[-16]
print(f"从字符串{my_str}取下标为2的元素的值是：{value}，取下标为-16的元素值是：{value2}")
#字符串不支持修改

#字符串index方法
value=my_str.index("and")
print(f"and起始下标是：{value}")

#replace的替换
new_my_str=my_str.replace("it","程序")
print(f"将字符串{my_str}替换得到新的字符串：{new_my_str}")

#字符串的分割
my_str="hello python itheima itcast"
my_str_list=my_str.split(" ")#括号里指的是空格进行分割
print(f"将字符串{my_str}在切分后得到：{my_str_list},得到的类型是：{type(my_str_list)}")

#字符串的规整操作
my_str="  itheima and itcast  "
new_my_str=my_str.strip()#不传入参数，默认去除首尾空格
print(f"将字符串{my_str}进行规整后得到{new_my_str}")

my_str="12itheima and itcast21"
new_my_str=my_str.strip("12")
print(f"通过对字符串{my_str}规整后得到”{new_my_str}")

#统计字符串中某个字符出现的次数，count
my_str="itheima and itcast"
count=my_str.count("it")
print(f"字符串{my_str}中it出现的次数：{count}")

#统计字符串的长度
num=len(my_str)
print(f"字符串中{my_str}中的长度是：{num}")
# 将数字类型转换为字符
str_type=str(11)
print(type(str_type),str_type)

float_str=str(11.345)
print(type(float_str),float_str)

#将字符转化为数字类型
num=int("11")
print(type(num),num)
num2=float("11.345")
print(type(num2),num2)

#整数转浮点数
float_num=float(num)
print(type(float_num),float_num)

#浮点数转整数
int_num=int(float_num)
print(type(int_num),int_num)

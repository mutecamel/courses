#使用print直接输出类型信息
print(type("黑马程序员"))
print(type(666))
print(type(11.345))

# 用变量保存type()语句的结果
string_type = type("黑马程序员")
int_type = type(666)
float_type = type(11.345)
print(string_type)
print(int_type)
print(float_type)

#方式三 使用type（）语句，看变量中保存的数据类型
name = "黑马程序员"
name_type=type(name)
print(name_type)

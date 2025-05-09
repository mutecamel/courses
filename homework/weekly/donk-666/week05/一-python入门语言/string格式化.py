# 用%占位
name="黑马程序员"
message="学IT，来:%s"%name
print(message)

#通过占位的形式，实现数字和string的拼接
class_num=21
avg_salary=17754
message="python大数据，北京%s期，毕业平均工资：%s元"%(class_num,avg_salary)
print(message)

#可以用%s,%d,%f分别实现对string，整数，浮点数的占位
name="传智播客"
set_up_year=2006
stock_price=19.99
message="我是：%s.我建立于:%d,我今天的股价是:%f"%(name,set_up_year,stock_price)
print(message)
num1=11
num2=11.345
print("数字11宽度限制为5，结果是：%5d"%num1)
print("数字11宽度限制为1，结果是：%1d"%num1)
print("数字11.345宽度限制7，小数精度2，结果是：%7.2f"%num2)
print("数字11.345小数精度2，结果是：%.2f"%num2)

#快速格式化
name="传智播客"
set_up_year=2006
stovk_prive=19.99
print(f"我是{name},我成立于{set_up_year},我的股价是{stovk_prive}元")
# if语句的基本格式
"""
age=int(input("age="))
if age>=18:
    print("我已经成年了")
    print("即将进如大学生活了")
print("时间过得真快")
"""

"""
#练习题
print("欢迎来到游乐园，儿童免费，成人收费")
age=int(input("请输入您的年龄："))
if age>=18:
    print("您已经成年")
print("祝您玩的愉快")
"""
"""
# if与else
print("欢迎来到游乐园，儿童免费，成人收费")
age=int(input("请输入您的年龄："))
if age>=18:
    print("您已经成年")
else:
    print("您未成年，可免费游玩")
print("祝您玩的愉快")
"""

# 练习题
"""
print("欢迎来到黑马程序员")
tall=int(input("请输入您的身高："))
if tall>130:
    print("您的身高超过130，游玩需要10元")
else:
    print("您的身高没有超过130，可以免费游玩")
print("祝您游玩愉快")
"""
"""
height=int(input("请输入你的身高："))
vip_level=int(input("请输入你的VIP等级："))
day=int(input("请输入今天的日期："))
if height<120:
    print("可以免费")
elif vip_level>3:
    print("可以免费")
elif day==1:
    print("可以免费")
else:
    print("需要购票")
"""
"""
#练习题
num=10
if int(input("请输入第一次猜想的数字："))==num:
    print("恭喜你猜对了")
elif int(input("不对，再来一次："))==num:
    print("对了")
elif int(input("不对，最后一次"))==num:
    print("恭喜")
else:
    print("都不对拉，我猜的数是%s"%num)
"""
# 嵌套判断语句：
if int(input("你的身高是多少：")) > 120:
    print("身高超过120，需要购票")
    print("但是如果您VIP等级大于3，可以免费游玩")
    if int(input("请输入您的VIP等级：")) > 3:
        print("vip等级够，可以免费游玩")
    else:
        print("要购票")
else:
    print("身高没有超过120，可免费游玩")

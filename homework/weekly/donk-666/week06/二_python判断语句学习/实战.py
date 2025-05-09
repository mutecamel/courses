import random
num=random.randint(1,10)
num1=int(input("请第一次输入数字："))
if num1==num:
    print("恭喜你猜对了")
else:
    print("没有猜对")
    if num1>num:
        print("你猜的数字大了")
    elif num1<num:
        print("你猜的数字小了")
    num2=int(input("请第二回输入数字："))
    if num2==num:
        print("恭喜你猜对了")
    else:
        print("没有猜对")
        if num2>num:
           print("你猜的数字大了")
        elif num2<num:
           print("你猜的数字小了")
        num3=int(input("请最后一次输入数字:"))
        if num3==num:
            print("恭喜你猜对了")
        else:
             print("三回都没有猜对，正确的数字是%d"%num)
# 在程序运行时，能保存计算结果或者能表示值的抽象概念。简单的说，变量就是在程序运行中，记录数据用的、

# 定义一个变量，用来记录钱包余额
money = 50
# 通过print语句输出来
print("钱包还有：",money)

#买了冰淇淋花了十元
money=money-10
print("买了冰激凌花了十元，还剩余：",money,"元")

#假设：每隔一小时输出钱包的余额
print("现在是下午1点，钱包余额剩余：",money,"元")
print("现在是下午2点，钱包余额剩余：",money,"元")
print("现在是下午3点，钱包余额剩余：",money,"元")
print("现在是下午4点，钱包余额剩余：",money,"元")

#练习
money=50
print("当前钱包余额：",money,"元")
bing=10
print("购买了冰淇淋，花费：",bing,"元")
voke=10
print("购买了可乐，花费：",voke,"元")
money=money-bing-voke
print("最终，钱包余额：",money,"元")


#定义两数相加的结果
"""
def add(x,y):
    result=x+y
    print(f"{x}+{y}的结果是：{result}")
add(5,71)
#函数的参数可以是任意个
"""
#案例题
def hesuan(x):
    if x>37.5:
        print("欢迎来到黑马程序员！")
        print(f"体温测量中，您的体温是：{x}度，需要隔离！")
    if x<=37.5:
        print("欢迎来到黑马程序员！")
        print(f"体温测量中，您的体温是：{x}度，体温合适，请进！")
now=input("请输入您的体温:")
hesuan(float(now))

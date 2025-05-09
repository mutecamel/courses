money=5000000
name=None
name=input("请输入您的姓名：")
def query(show_header):
    if show_header:
        print("-----------------查询----------------")
    print(f"{name},您好，您的余额剩余：{money}元")
def saving(num):
     global money
     money+=num
     print("------------存款----------------")
     print(f"{name},您好，您存款{num}元成功")
     query(False)
def get_money(num):
    global money
    money += num
    print("------------取款----------------")
    print(f"{name},您好，您取款{num}元成功")
    query(False)
def main():
    print("------------主菜单----------------")
    print(f"{name},您好，欢迎来到黑马ATM,请选择操作")
    print("查询余额\t[输入1]")
    print("存款\t\t[输入2]")
    print("取款\t\t[输入3]")
    print("退出\t\t[输入4]")
    return input("请输入您的选择：")
while True:
    keyboard=main()
    if keyboard=="1":
        query(True)
        continue
    elif keyboard=="2":
        num=int(input("您想要存多少钱？请输入："))
        saving(num)
        continue
    elif keyboard=="3":
        num=int(input("您想要取多少钱？请输入："))
        get_money(num)
        continue
    else:
        print("程序退出")
        break







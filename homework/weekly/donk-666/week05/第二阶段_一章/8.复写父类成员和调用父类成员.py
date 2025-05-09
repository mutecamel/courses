#复写：在子类中重新定义同名的属性和方法即可
class Phone:
    IMEI=None #序列号
    producer="ITCAST"#厂商
    def call_by_5g(self):
        print("使用5g网络通话")
#定义子类，复写父类成员：
class MyPhone(Phone):
    producer = "ITheima"
    def call_by_5g(self):
        print("开启CPU单核模式，确保通话时省电")
        print(f"父类的厂商是：{super().producer}") #super()可以调用父类的
        super().call_by_5g()
        print("关闭CPU单核模式，确保性能")
phone=MyPhone()
phone.call_by_5g()
print(phone.producer)

#调用父类成员

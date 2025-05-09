#定义一个类，内涵私有成员变量和私有成员方法
#私有成员无法被类对象使用，但是可以被其他的成员使用
class Phone:
    __current_voltage = 0.5  # 当前手机的运行电压

    def __keep_single_core(self):
        print("让CPU以单核模式运行")

    def call_by_5G(self):
        if self.__current_voltage >= 1:
            print("5g通话已经开启")
        else:
            self.__keep_single_core()  # 正确调用私有成员方法，不需要传递self
            print("电量不足，无法使用5g通话，并已设置已单核模式运行")


phone = Phone()
phone.call_by_5G()  # 调用公开方法
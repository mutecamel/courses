#构造方法的名称：__init__
class Student:
    name=None
    age=None
    tel=None
    def __init__(self,name,age,tel):
        self.name=name #访问类的成员变量
        self.age=age
        self.tel=tel
        print(f"student类创建了一个类对象")

stu=Student("周杰伦","31","18295970421")
print(stu.name)
print(stu.age)
print(stu.tel)




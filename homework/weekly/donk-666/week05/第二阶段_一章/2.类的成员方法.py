#定义一个带有成员方法的类
class Student:
    name=None #学生的姓名
    def say_hi(self):
        print(f"大家好，我是{self.name}，希望大家多多多多关照")
    def say_hi2(self,msg):
        print(f"大家好，我是{self.name},{msg}")
stu=Student()
stu.name="周杰伦"
stu.say_hi2("欧呦，不错哦")

stu2=Student()
stu2.name="林俊杰"
stu2.say_hi2("小伙子我看好你")
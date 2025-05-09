class Student():
    def __init__(self,name,age):
        self.name=name #学生姓名
        self.age=age#学生年龄
    #__str__魔术方法
    def __str__(self):
        return f"Student的类对象，name:{self.name},age:{self.age}"
    #__it__魔术方法

    def __lt__(self,other):
        return self.age<other.age

    #__le__魔术方法
    def __le__(self,other):
        return self.age<=other.age
    #__eq__魔术方法
    def __eq__(self):
        return self.age==other.age
stu1=Student("周杰伦",31)
stu2=Student("林俊杰",33)
print(stu1<=stu2)
print(stu1>=stu2)


class Student:
    def __init__(self,name,age,addr):
        self.name=name
        self.age=age
        self.addr=addr
        print(name,age,addr)
students=[]
for i in range(10):
    print(f"当前录入的是第{i+1}位学生的信息，总过需要录入十位学生信息")
    name_data=input("请输入学生姓名：")
    age_data=input("请输入学生年龄：")
    addr_data=input("请输入学生地址：")
    stu = Student(name_data,age_data,addr_data)
    students.append(stu)
# 现在，students列表包含了十位学生的信息
# 您可以根据需要对学生列表进行进一步的操作，比如打印所有学生的信息
for student in students:
    print(f"姓名：{student.name}，年龄：{student.age}，地址：{student.addr}")



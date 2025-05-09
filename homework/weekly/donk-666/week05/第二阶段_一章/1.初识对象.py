# 设计一个类（类比生活中：设计一张登记表）
class Student:
    name = None  # 记录学生姓名
    gender = None  # 记录学生性别
    nationality = None  # 记录学生国籍
    native_place = None  # 记录学生籍贯
    age = None  # 记录学生年龄


# 创建一个对象（类比生活中：打印一张登记表）
stu_1 = Student()
# 对象属性进行赋值（类比生活中：填写表单）
stu_1.name = "林俊杰"
stu_1.gender = "男"
stu_1.nationality = "中国"
stu_1.native_place = "山东省"
stu_1.age = 31
# 获取对象中记录的信息
print(stu_1.name)
print(stu_1.gender)
print(stu_1.nationality)
print(stu_1.native_place)
print(stu_1.age)

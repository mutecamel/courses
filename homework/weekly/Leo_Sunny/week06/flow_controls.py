# for循环例子
# 1.遍历列表
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
# 2.遍历字符串
message = "Hello"
for char in message:
    print(char)
# 3.range函数
for i in range(5):
    print(i)
# 4.遍历字典
student = {"name": "Alice", "age": 20, "grade": "A"}
for key, value in student.items():
    print(f"{key}: {value}")

student = {"name": "Alice", "age": 20, "grade": "A"}
for key in student.keys():
    print(f"{key}")

student = {"name": "Alice", "age": 20, "grade": "A"}
for value in student.values():
    print(f"{value}")


# while循环例子
# 1.简单计数
count = 0
while count < 5:
    print(count)
    count = count + 1

# 2.循环处理列表元素
my_list = [10, 20, 30, 40, 50]
index = 0
while index < len(my_list):
    print(my_list[index])
    index = index + 1

# 3.循环读取用户信息
number = int(input("请输入一个数字（输入 0 退出）: "))
while number != 0:
    print(f"你输入的数字是: {number}")
    number = int(input("请输入一个数字（输入 0 退出）: "))
print("循环结束。")


# try和raise配合举例
def divide_numbers():
    try:
        num1 = float(input("请输入被除数: "))
        num2 = float(input("请输入除数: "))
        if num2 == 0:
            raise ZeroDivisionError("除数不能为零")
        result = num1 / num2
        print(f"结果是: {result}")
    except ValueError:
        print("输入无效，请输入有效的数字。")
    except ZeroDivisionError as e:
        print(f"捕获到异常: {e}")


divide_numbers()

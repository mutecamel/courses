fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    fruit += ",ok"
    print(fruit)

message = "Hello"
for char in message:
    print(char)

person = {"name": "John", "age": 30, "city": "New York"}
for key in person:
    print(key, ":", person[key])

for i in range(5):
    print(i)

for i in range(3):
    for j in range(2):
        print(i, j)

# while语句
count = 0
while count < 5:
    print(count)
    count = count + 1

user_input = ""
while user_input != "quit":
    user_input = input("请输入内容（输入 'quit' 退出）：")
    if user_input != "quit":
        print(f"你输入的是: {user_input}")

numbers = [1, 2, 3, 4, 5]
while numbers:
    current_number = numbers.pop(0)
    print(f"正在处理数字: {current_number}")

# break语句
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num == 3:
        break
    print(num)  # 在 for 循环中使用 break 语句

# Continue语句
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num % 2 == 0:
        continue
    print(num)

# For…else循环
fruits = ["apple", "banana", "cherry"]
search_fruit = "mango"
for fruit in fruits:
    if fruit == search_fruit:
        print(f"找到了 {search_fruit}。")
        break
else:
    print(f"没有找到 {search_fruit}。")

# If语句
age = 20
is_student = True
if age >= 18 and is_student:
    print("你是成年学生。")

# If…elif[…elif]多重条件分支
score = 85

if score >= 90:
    print("成绩等级：A")
elif score >= 80:
    print("成绩等级：B")
elif score >= 70:
    print("成绩等级：C")
elif score >= 60:
    print("成绩等级：D")
else:
    print("成绩等级：F")

# If…else未满足条件的处理
number = -5
if number >= 0:
    print(f"{number} 是正数或零。")
else:
    print(f"{number} 是负数。")

# Try…except[…except…else…finally]捕捉异常的处理
try:
    num1 = int(input("请输入一个被除数: "))
    num2 = int(input("请输入一个除数: "))
    result = num1 / num2
except ValueError:
    print("输入无效，请输入有效的整数。")
except ZeroDivisionError:
    print("错误：除数不能为零。")
else:
    print(f"结果是: {result}")
finally:
    print("操作完成。")


# Raise主动抛出异常
class CustomError(Exception):
    pass


def check_number(num):
    if num % 2 != 0:
        raise CustomError("输入的数字必须是偶数。")
    return num


try:
    number = check_number(3)
    print(f"输入的数字是: {number}")
except CustomError as e:
    print(f"发生自定义错误: {e}")

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"I like {fruit}")

message = "hello"
for char in message:
    print(char)

count = 0
while count < 5:
    print(f"当前计数: {count}")
    count += 1

count = 0
while count < 10:
    count += 1
    if count == 5:
        continue  # 跳过本次循环剩余部分，继续下一次循环
    if count == 8:
        break  # 终止整个循环
    print(f"当前计数: {count}")

numbers = [10, 20, 30, 40, 50]
target = 60
for num in numbers:
    if num == target:
        print(f"找到了目标数字 {target}")
        break
else:
    print(f"没有找到目标数字 {target}")

age = 18
if age >= 18:
    print("你已经成年了，可以参加投票。")

score = 85
if score >= 90:
    print("你的成绩等级是 A。")
elif score >= 80:
    print("你的成绩等级是 B。")
elif score >= 70:
    print("你的成绩等级是 C。")
elif score >= 60:
    print("你的成绩等级是 D。")
else:
    print("你的成绩不及格。")

num = -3
if num > 0:
    print(f"{num} 是正数")
else:
    print(f"{num} 是负数或者零")

try:
    num = 10 / 0
    print(num)
except ZeroDivisionError:
    print("除数不能为零！")


try:
    num = int(input("请输入一个整数: "))
    result = 10 / num
except ZeroDivisionError:
    print("除数不能为零！")
except ValueError:
    print("输入的不是一个有效的整数！")
else:
    print(f"计算结果是: {result}")
finally:
    print("无论是否有异常，这个都会被执行。")


def check_age(age):
    if age < 0:
        raise ValueError("年龄不能为负数")
    return f"你的年龄是 {age} 岁"


try:
    result = check_age(-5)
    print(result)
except ValueError as e:
    print(e)


def add_numbers(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("输入的参数必须是数字类型（int 或 float）")
    return a + b


try:
    result = add_numbers(5, "3")
    print(result)
except TypeError as e:
    print(e)

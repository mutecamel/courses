fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    fruit = fruit + ",delicious"
    print(fruit)

message = "Hello"
for char in message:
    print(char)

for i in range(6):
    print(i)

student = {"name": "John", "age": 20, "grade": "A"}
for key in student:
    print(key, ":", student[key])

student = {"name": "John", "age": 20, "grade": "A"}
for value in student.values():
    print(value)

count = 0
while count < 5:
    print(count)
    count = count + 1

numbers = [1, 2, 3, 4, 5]
while numbers:
    print(numbers.pop())

import random

secret_number = random.randint(1, 10)
guess = None
while guess != secret_number:
    guess = int(input("猜一个 1 到 10 之间的数字: "))
    if guess < secret_number:
        print("猜的数字太小了，再试一次！")
    elif guess > secret_number:
        print("猜的数字太大了，再试一次！")
print("恭喜你，猜对了！")


numbers = [2, 4, 6, 8, 10]
target = 3

for num in numbers:
    if num == target:
        print(f"找到了目标数字 {target}")
        break
else:
    print(f"未找到目标数字 {target}")


score = 85
if score >= 90:
    print("成绩等级为 A。")
elif score >= 80:
    print("成绩等级为 B。")
elif score >= 70:
    print("成绩等级为 C。")
elif score >= 60:
    print("成绩等级为 D。")
else:
    print("成绩等级为 F。")


month = 7
if 3 <= month <= 5:
    season = "春季"
elif 6 <= month <= 8:
    season = "夏季"
elif 9 <= month <= 11:
    season = "秋季"
elif month == 12 or 1 <= month <= 2:
    season = "冬季"
else:
    season = "输入的月份不合法"
print(f"{month} 月属于 {season}。")

num = -5
if num >= 0:
    print(f"{num} 是一个非负数。")
else:
    print(f"{num} 是一个负数。")


try:
    num = int("abc")
except ValueError:
    print("错误：输入不是有效的整数！")
except ZeroDivisionError:
    print("错误：不能除以零！")


numbers = [1, 2, -3, 4, 5]
for num in numbers:
    if num < 0:
        raise ValueError(f"发现负数: {num}")
    print(num)

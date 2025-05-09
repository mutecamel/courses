fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)


message = "Hello"
for char in message:
    print(char)


for i in range(5):
    print(i)


person = {"name": "John", "age": 30, "city": "New York"}
for key in person:
    print(key, ":", person[key])


count = 0
while count < 5:
    print(count)
    count = count + 1


total = 0
number = int(input("请输入一个数字（输入 0 结束）: "))
while number != 0:
    total = total + number
    number = int(input("请输入一个数字（输入 0 结束）: "))
print("数字总和为:", total)


import random

secret_number = random.randint(1, 10)
guess = None
while guess != secret_number:
    guess = int(input("猜一个 1 到 10 之间的数字: "))
    if guess < secret_number:
        print("猜的数字太小了，再试一次。")
    elif guess > secret_number:
        print("猜的数字太大了，再试一次。")
print("恭喜你，猜对了！")


num = input("请输入一个正数: ")
try:
    num = float(num)
    if num <= 0:
        raise ValueError("输入的不是正数")
    print(f"输入的正数是: {num}")
except ValueError as e:
    print(f"发生错误: {e}")

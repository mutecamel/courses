fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    fruit = fruit + ",ok"
    print(fruit)

message = "Hello"
for char in message:
    print(char)

for i in range(3):
    for j in range(2):
        print(i, j)

student = {"name": "John", "age": 20, "grade": "A"}
# 遍历字典的键
for key in student:
    print(key)

# 遍历字典的值
for value in student.values():
    print(value)

# 遍历字典的键值对
for key, value in student.items():
    print(key, ":", value)

count = 0
while count < 5:
    print(count)
    count = count + 1

valid_input = False
while not valid_input:
    try:
        num = int(input("请输入一个整数: "))
        valid_input = True
        print(f"你输入的有效整数是: {num}")
    except ValueError:
        print("输入无效，请输入一个整数。")


import random  # noqa: E402

number = random.randint(1, 10)
guess = None
while guess != number:
    guess = int(input("猜一个 1 到 10 之间的数字: "))
    if guess < number:
        print("猜的数字太小了，再试一次。")
    elif guess > number:
        print("猜的数字太大了，再试一次。")
    else:
        print("恭喜你，猜对了！")

numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num == 3:
        break
    print(num)

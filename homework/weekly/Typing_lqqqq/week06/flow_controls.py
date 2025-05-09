# for 迭代循环 (iteration loop)
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    fruit = fruit + ",ok"
    print(fruit)

message = "Hello"
for char in message:
    print(char)

for i in range(5):  # 从0开始到4
    print(i)

student = {"name": "Alice", "age": 20, "grade": "A"}
for key, value in student.items():
    print(f"{key}: {value}")

student = {"name": "Alice", "age": 20, "grade": "A"}
for key in student.keys():
    print(key)

student = {"name": "Alice", "age": 20, "grade": "A"}
for value in student.values():
    print(value)

# while 条件循环 (conditional loop)
# 基本计数循环
count = 0
while count < 5:
    print(count)
    count = count + 1
#
number = [1, 2, 3, 4, 5]
while count < 5:
    print(count)
    count = count + 1

# 条件判断循环
user_input = ""
while user_input != "quit":
    user_input = input("请输入内容（输入 'quit' 退出）：")
    if user_input != "quit":
        print(f"你输入的是：{user_input}")

# 循环读取用户输入
i = 0
while i < 3:
    j = 0
    while j < 2:
        print(f"i = {i}, j = {j}")
        j = j + 1
    i = i + 1


# break 打断跳出循环
# continue 跳至下一轮循环
# for...else 循环未被打断的处理
# if 条件分支
# if...elif[...elif] 多重条件分支
# if...else 未满足条件的处理
# try...except[...except...else...finally] 捕捉异常的处理
# raise 主动抛出异常

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    fruit += ", ok"
    print(fruit)

message = "hello"
for char in message:
    print(char)
# 输出：
# apple
# banana
# cherry

person = {"name": "Alice", "age": 25, "city": "New York"}
for key, value in person.items():
    print(f"{key}: {value}")
# 输出：
# name: Alice
# age: 25
# city: New York

count = 1
while count <= 5:
    print(count)
    count += 1
# 输出：1 2 3 4 5

while True:
    user_input = input("输入内容（输入 'q' 退出）：")
    if user_input == 'q':
        print("退出循环")
        break
    print(f"你输入了：{user_input}")

while True:
    user_input = input("请输入一个整数：")
    if user_input.isdigit():  # 检查是否为数字
        num = int(user_input)
        print(f"你输入的整数是：{num}")
        break
    else:
        print("输入无效，请重新输入！")

def check_positive(num):
    if num <= 0:
        raise ValueError("数字必须是正数")
    return num

try:
    result = check_positive(-5)
except ValueError as e:
    print(f"捕获异常：{e}")  # 输出：捕获异常：数字必须是正数

try:
    # 获取用户输入并转换为整数
    num = int(input("请输入 1 到 100 之间的整数："))
    # 检查输入是否符合范围，不符合则抛出异常
    if num < 1 or num > 100:
        raise ValueError("输入的数字必须在 1 到 100 之间")
    print(f"你输入的数字是 {num}，符合要求！")
except ValueError as ve:
    # 捕获并处理值错误（输入范围不正确）
    print(f"值错误：{ve}")
except Exception as e:
    # 捕获其他意外异常（如输入非数字）
    print(f"发生其他错误：{e}")
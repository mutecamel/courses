# 遍历列表中的元素
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# 打印 0 到 4（不包含 5）
for i in range(5):
    print(i)

# 指定起始和步长（输出 2,4,6,8）
for i in range(2, 10, 2):
    print(i)


# 遍历字典的键和值
person = {"name": "Alice", "age": 25, "city": "New York"}
for key, value in person.items():
    print(f"{key}: {value}")

# 从 1 数到 5
count = 1
while count <= 5:
    print(count)
    count += 1  # 等价于 count = count + 1


# 要求用户输入 "yes" 才继续
user_input = ""
while user_input.lower() != "yes":
    user_input = input('请输入 "yes" 继续: ')
print("程序继续执行！")


# 输入 "quit" 退出循环
while True:
    command = input("输入命令 (输入 quit 退出): ")
    if command == "quit":
        break
    print(f"执行命令: {command}")
print("循环结束")



def check_age(age):
    try:
        if age < 0:
            raise ValueError("年龄不能为负数！")  # 主动抛出异常
        elif age < 18:
            print("未成年人")
        else:
            print("成年人")
    except ValueError as e:
        print(f"错误：{e}")

check_age(25)  # 输出: 成年人
check_age(-5)  # 输出: 错误：年龄不能为负数！
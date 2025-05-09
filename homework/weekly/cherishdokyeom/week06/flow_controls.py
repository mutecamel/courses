# for

# 遍历列表
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    fruit += ",OK"
    print(fruit)

# 遍历字符串
message = "Hello"
for char in message:
    print(char)

# 结合range()函数
for i in range(5):
    print(i)

# 遍历字典
person = {"name": "John", "age": 30, "city": "New York"}
for key in person:  # person.keys()键 person.values()值
    print(key, ":", person[key])

# while

# 简单计数循环
i = 0
while i < 5:
    print(i)
    i = i + 1

# 处理列表元素
numbers = [1, 2, 3, 4, 5]
while numbers:
    print(numbers.pop())

# 验证用户输入
valid_input = False
while not valid_input:
    try:
        num = int(input("请输入一个整数: "))
        valid_input = True
    except ValueError:
        print("输入无效，请输入一个整数。")

print("你输入的整数是:", num)

# if...elif[...elif] 多重条件分支
# 门票价格计算
age = 30
is_member = True

if age < 12:
    price = 0  # 儿童免费
elif 12 <= age <= 65:
    price = 20 if not is_member else 10  # 会员半价
else:
    price = 15  # 老年人优惠

print(f"Ticket price: ${price}")  # 输出：$10（会员享受折扣）

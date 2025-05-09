fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    fruit=fruit+",ok"
    print(fruit)

    message = "Hello"
for char in message:
    print(char)

    student = {
    "name": "John",
    "age": 20,
    "grade": "A"
}
# 遍历字典的键
for key in student:
    print(key)

# 遍历字典的值
for value in student.values():
    print(value)

# 遍历字典的键值对
for key, value in student.items():
    print(f"{key}: {value}")

    # 打印 0 到 4 的数字
for i in range(5):
    print(i)

# 打印 2 到 6 的数字
for i in range(2, 7):
    print(i)

# 打印 1 到 10 之间的奇数
for i in range(1, 11, 2):
    print(i)


for i in range(3):
    for j in range(2):
        print(f"({i}, {j})")

count = 0
while count < 5:
    print(count)
    count += 1

i = 0
while i < 10:
    i += 1
    if i % 2 == 1:  # 如果是奇数
        continue
    print(i)

count = 0
while count < 3:
    print(count)
    count += 1
else:
    print("循环结束")

numbers = [1, 3, 5, 7, 9]
for num in numbers:
    if num % 2 == 0:
        print(f"找到了偶数 {num}")
        break
else:
    print("列表中没有偶数")

try:
    num = int(input("请输入一个整数: "))
    result = 10 / num
    print(f"结果是: {result}")
except ValueError:
    print("输入的不是有效的整数，请重新输入。")
except ZeroDivisionError:
    print("除数不能为零，请输入一个非零的整数。")

# 定义一个函数用于计算两个数的商
def divide_numbers(a, b):
    if b == 0:
        # 当除数为 0 时，主动抛出 ZeroDivisionError 异常
        raise ZeroDivisionError("除数不能为零")
    return a / b

try:
    result = divide_numbers(10, 0)
    print(result)
except ZeroDivisionError as e:
    print(f"捕获到异常: {e}")

# 定义一个自定义异常类，继承自 Exception
class NegativeNumberError(Exception):
    pass

# 定义一个函数用于计算一个数的平方根
def calculate_square_root(num):
    if num < 0:
        # 当输入的数为负数时，主动抛出自定义异常
        raise NegativeNumberError("不能对负数计算平方根")
    return num ** 0.5

try:
    result = calculate_square_root(-4)
    print(result)
except NegativeNumberError as e:
    print(f"捕获到异常: {e}")

def check_age(age):
    if age < 0:
        # 抛出异常时携带额外的字典信息
        raise ValueError("年龄不能为负数", {"输入的年龄": age})
    elif age > 120:
        raise ValueError("年龄不太可能超过 120 岁", {"输入的年龄": age})
    return age

try:
    result = check_age(-5)
    print(result)
except ValueError as e:
    print(f"捕获到异常: {e.args[0]}")
    if len(e.args) > 1:
        print(f"额外信息: {e.args[1]}")

def get_valid_integer():
    while True:
        try:
            user_input = input("请输入一个正整数: ")
            num = int(user_input)
            if num <= 0:
                raise ValueError("输入的数必须是正整数。")
            return num
        except ValueError as e:
            print(f"输入无效: {e}")


valid_num = get_valid_integer()
print(f"你输入的有效正整数是: {valid_num}")

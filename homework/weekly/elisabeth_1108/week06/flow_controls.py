fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

message = "Hello"
for char in message:
    print(char)

numbers = (1, 2, 3, 4, 5)
for num in numbers:
    print(num)

student = {"name": "John", "age": 20, "grade": "A"}
for key in student:
    print(key, student[key])

for i in range(5):
    print(i)

numbers = [1, 2, 3, 4, 5, 6]
for num in numbers:
    if num == 6:
        print("Found 6!")
        break
else:
    print("6 not found.")

# 简单循环计数
count = 1
while count <= 5:
    print(count)
    count = count + 1

# 从用户输入中累加数字
total = 0
number = int(input("请输入一个数字（输入 0 结束）: "))
while number != 0:
    total = total + number
    number = int(input("请输入一个数字（输入 0 结束）: "))
print("所有输入数字的总和是:", total)


# 定义一个列表
numbers = [1, 2, 3, 4, 5]
# 遍历列表
for num in numbers:
    if num == 3:
        # 当 num 等于 3 时，跳出循环
        break
    print(num)

# 在 while 循环中使用 continue
# 计算 1 到 10 之间奇数的和
total = 0
i = 1
while i <= 10:
    if i % 2 == 0:
        i = i + 1
        continue
    total = total + i
    i = i + 1

print(total)

# 在 for 循环中使用 continue
# 打印 1 到 10 之间的奇数
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)

# 检查列表中是否存在特定元素
numbers = [1, 2, 3, 4, 5]
target = 6

for num in numbers:
    if num == target:
        print(f"找到了目标数字 {target}")
        break
else:
    print(f"未找到目标数字 {target}")

# 判断一个数是否为质数
num = 17
if num < 2:
    print(f"{num} 不是质数")
else:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            print(f"{num} 不是质数")
            break
    else:
        print(f"{num} 是质数")

# 嵌套的 if 语句
age = 16
gender = "男"
if age >= 18:
    if gender == "男":
        print("成年男性。")
    else:
        print("成年女性。")
else:
    print("未成年。")

# if...elif[...elif] 多重条件分支
# 依据用户输入的季节名称输出对应信息
season = input("请输入一个季节名称（春、夏、秋、冬）：")

if season == "春":
    print("春天是万物复苏的季节。")
elif season == "夏":
    print("夏天是炎热多雨的季节。")
elif season == "秋":
    print("秋天是丰收的季节。")
elif season == "冬":
    print("冬天是寒冷的季节。")
else:
    print("输入的季节名称有误。")

# if...else 未满足条件的处理
#  例 1：判断数字正负
num = -5
if num >= 0:
    print("这个数字是正数或零。")
else:
    print("这个数字是负数。")


# try...except[...except...else...finally]
try:
    # 可能会引发异常的代码
    num1 = int(input("请输入一个整数: "))
    num2 = int(input("请输入另一个整数: "))
    result = num1 / num2
except ValueError:
    # 处理输入非整数的异常
    print("输入无效，请输入整数。")
except ZeroDivisionError:
    # 处理除数为零的异常
    print("错误：除数不能为零。")
else:
    # 如果没有异常，执行此块
    print(f"结果是: {result}")
finally:
    # 无论是否有异常，都会执行此块
    print("程序结束。")


#  抛出内置异常
def validate_age(age):
    if age < 0:
        raise ValueError("年龄不能为负数")
    return age


#  抛出自定义异常
try:
    age = validate_age(-5)
except ValueError as e:
    print(f"捕获到异常: {e}")


class MyCustomError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


def check_number(num):
    if num > 100:
        raise MyCustomError("数字不能超过 100")
    return num


try:
    number = check_number(105)
except MyCustomError as e:
    print(f"捕获到自定义异常: {e}")

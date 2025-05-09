# for语句
fruits = ["pear", "grape", "lemon"]
for fruit in fruits:
    print(fruit)

fruits = ["pear", "grape", "lemon"]
for fruit in fruits:
    fruit += ", good"
    print(fruit)  # 遍历列表

message = "Python"
for char in message:
    print(char)  # 遍历字符串

for i in range(7):
    print(i)  # 结合range函数

student = {"name": "Bob", "age": 22, "grade": "B"}
for key, value in student.items():
    print(f"{key}: {value}")  # 遍历字典

student = {"name": "Bob", "age": 22, "grade": "B"}
for value in student.values():
    print(value)  # 遍历字典

# while语句
count = 3
while count < 8:
    print(count)
    count = count + 1  # 简单计数

numbers = [6, 7, 8, 9, 10]
while numbers:
    print(numbers.pop())  # 从列表中移除元素

valid_input = False
while not valid_input:
    user_input = input("请输入一个大于 20 的数字: ")
    try:
        num = int(user_input)
        if num > 20:
            print("输入有效。")
            valid_input = True
        else:
            print("输入的数字必须大于 20，请重新输入。")
    except ValueError:
        print("输入无效，请输入一个有效的数字。")  # 用户输入验证

# break语句
fruits = ["pear", "grape", "lemon", "mango"]
for fruit in fruits:
    if fruit == "lemon":
        break
    print(fruit)  # 在 for 循环中使用 break

count = 2
while count < 12:
    if count == 7:
        break
    print(count)
    count = count + 1  # 在 while 循环中使用 break

for i in range(4):
    for j in range(4):
        if i + j == 3:
            break
        print(f"({i}, {j})")  # 嵌套循环中使用 break

# continue语句
numbers = [6, 7, 8, 9, 10]
for num in numbers:
    if num == 8:
        continue
    print(num)  # 在 for 循环中使用 continue

count = 3
while count < 8:
    count = count + 1
    if count == 5:
        continue
    print(count)  # 在 while 循环中使用 continue

count = 3
while count < 8:
    count = count + 1
    if count == 5:
        continue
    print(count)  # 嵌套循环中使用 continue

# for...else语句
numbers = [2, 4, 6, 8, 10]
for num in numbers:
    if num % 2 != 0:
        print(f"找到了奇数: {num}")
        break
else:
    print("列表中没有奇数。")  # 查找列表中的奇数

text = "Python is great"
target = "k"
for char in text:
    if char == target:
        print(f"找到了字符 '{target}'。")
        break
else:
    print(f"字符串中没有字符 '{target}'。")  # 检查字符串中是否包含特定字符

student_scores = {"Alice": 92, "Bob": 87, "Charlie": 75}
search_name = "Eve"
for name in student_scores.keys():
    if name == search_name:
        print(f"找到了 {search_name}，分数是 {student_scores[search_name]}。")
        break
else:
    print(f"没有找到 {search_name} 的记录。")  # 遍历字典的键

# if语句
age = 21
if age >= 20:
    print("你已经是成熟的成年人了。")  # 简单的 if 语句

num = 15
if num % 2 == 0:
    print(f"{num} 是偶数。")
else:
    print(f"{num} 是奇数。")  # if-else 语句

score = 92
if score >= 95:
    print("成绩为 A+。")
elif score >= 90:
    print("成绩为 A。")
elif score >= 80:
    print("成绩为 B。")
elif score >= 70:
    print("成绩为 C。")
elif score >= 60:
    print("成绩为 D。")
else:
    print("成绩为 F。")  # if-elif-else 语句

is_member = False
money = 250
product_price = 220
if is_member:
    if money >= product_price:
        print("你是会员，且余额足够，可以购买该商品。")
    else:
        print("你是会员，但余额不足，无法购买该商品。")
else:
    if money >= product_price:
        print("你不是会员，但余额足够，可以购买该商品。")
    else:
        print("你不是会员，且余额不足，无法购买该商品。")  # 嵌套的 if 语句

# if...elif语句
month = 10
if 3 <= month <= 5:
    print("当前季节是春季")
elif 6 <= month <= 8:
    print("当前季节是夏季")
elif 9 <= month <= 11:
    print("当前季节是秋季")
elif month == 12 or 1 <= month <= 2:
    print("当前季节是冬季")
else:
    print("输入的月份无效")

# if...else语句
number = 17
if number % 2 == 0:
    print(f"{number} 是偶数。")
else:
    print(f"{number} 是奇数。")

# try...except语句
try:
    result = 15 / 0
    print(result)
except ZeroDivisionError:
    print("错误：除数不能为零。")

# try...except...else...finally语句
try:
    num1 = int(input("请输入第一个整数: "))
    num2 = int(input("请输入第二个整数: "))
    result = num1 / num2
except ValueError:
    print("输入错误：请输入有效的整数。")
except ZeroDivisionError:
    print("错误：除数不能为零。")
else:
    print(f"除法运算结果是: {result}")
finally:
    print("无论是否发生异常，此代码块都会执行。")


# raise语句
def divide_numbers(a, b):
    if b == 0:
        raise ZeroDivisionError("除数不能为零。")
    return a / b


try:
    result = divide_numbers(15, 0)
    print(result)
except ZeroDivisionError as e:
    print(f"捕获到异常: {e}")

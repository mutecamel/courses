# for语句 #
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    fruit += ", delicious"
    print(fruit)

message = "Hello"
for char in message:
    print(char)

    # 打印0到4的整数
for i in range(5):
    print(i)

student = {"name": "John", "age": 20, "grade": "A"}
for key, value in student.items():
    print(key, ":", value)

student = {"name": "John", "age": 20, "grade": "A"}
for key in student.keys():
    print(key, ":", value)

student = {"name": "John", "age": 20, "grade": "A"}
for value in student.values():
    print(key, ":", value)

# while语句 #
count = 0
while count < 5:
    print(count)
    count = count + 1

numbers = [1, 2, 3, 4, 5]
while numbers:
    print(numbers.pop())

sum_result = 0
number = 1
while number <= 10:
    sum_result = sum_result + number
    number = number + 1
print("1 到 10 的整数之和为:", sum_result)

# continue语句 #
# for循环
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in numbers:
    if num % 2 != 0:
        continue
print(num)

# while循环
total = 0
number = 0
while number < 10:
    number = number + 1
    if number % 2 != 0:
        continue
    total = total + number
print(total)

# 嵌套循环
for i in range(1, 6):
    for j in range(1, 6):
        if i % 2 != 0 and j % 2 != 0:
            continue
        print(f"{i} x {j} = {i * j}")

# break语句 #
# for循环
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in numbers:
    if num == 5:
        print(f"找到了数字 {num}，停止查找。")
        break
    print(num)

# while循环
import random

secret_number = random.randint(1, 10)
attempts = 0
while attempts < 3:
    guess = int(input("请猜一个 1 到 10 之间的数字："))
    attempts = attempts + 1
    if guess == secret_number:
        print("恭喜你，猜对了！")
        break
    else:
        print("猜错了，再试一次。")
else:
    print(f"很遗憾，你的机会用完了，正确答案是 {secret_number}。")

# 嵌套循环
matrix = [[10, 11, 12], [13, 14, 15], [16, 17, 20]]
found = False
for row in matrix:
    for num in row:
        if num == 20:
            print(f"找到了数字 {num}，停止查找。")
            found = True
            break
    if found:
        break

# for..else语句
numbers = [1, 2, 3, 4, 5]
target = 6
for num in numbers:
    if num == target:
        print(f"找到了 {target}")
        break
else:
    print(f"未找到 {target}")

# if语句
age = 20
if age >= 18:
    print("你已经成年了。")

# if..elif语句
score = 78
if score >= 90:
    print("成绩等级：A")
elif score >= 80:
    print("成绩等级：B")
elif score >= 70:
    print("成绩等级：C")
elif score >= 60:
    print("成绩等级：D")
else:
    print("成绩等级：F")

# if..else语句
num = 10
if num % 2 == 0:
    print(f"{num} 是偶数。")
else:
    print(f"{num} 是奇数。")

# try语句 #
try:
    num1 = 10
    num2 = 0
    result = num1 / num2
    file = open("nonexistent_file.txt", "r")
    content = file.read()
except ZeroDivisionError:
    print("错误：除数不能为零。")
except FileNotFoundError:
    print("错误：未找到指定的文件。")

try:
    num = 1 / 0
except Exception as e:
    print(f"发生了未知错误：{e}")

# try..except语句
try:
    num = int("abc")
    print(num)
except ValueError:
    print("输入的内容不能转换为整数，请输入有效的数字。")

# try..except..else
try:
    num = int("123")
except ValueError:
    print("输入的内容不能转换为整数，请输入有效的数字。")
else:
    print(f"成功将输入转换为整数，结果是 {num}。")

# try..except..finally
file = None
try:
    file = open("test.txt", "w")
    file.write("Hello, World!")
except IOError:
    print("文件操作出现错误。")
finally:
    if file:
        file.close()
    print("文件操作结束。")


# raise语句
# 内置异常
def divide_numbers(a, b):
    if b == 0:
        raise ZeroDivisionError("除数不能为零。")
    return a / b


try:
    result = divide_numbers(10, 0)
    print(result)
except ZeroDivisionError as e:
    print(f"捕获到异常: {e}")


# 自定义异常
class NegativeNumberError(Exception):
    def __init__(self, message="输入不能为负数。"):
        self.message = message
        super().__init__(self.message)


def square_root(num):
    if num < 0:
        raise NegativeNumberError()
    return num**0.5


try:
    result = square_root(-4)
    print(result)
except NegativeNumberError as e:
    print(f"捕获到异常: {e}")

# 循环中的异常
numbers = [1, 2, 3, 4, 5]
target = 6
for num in numbers:
    if num == target:
        print(f"找到了 {target}")
        break
else:
    raise ValueError(f"{target} 不在列表中。")

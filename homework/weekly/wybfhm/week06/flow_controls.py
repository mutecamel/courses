fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    fruit = fruit + ", ok"
    print(fruit)

message = "Hello"
for char in message:
    print(char)

for i in range(5):
    print(i)

person = {"name": "John", "age": 30, "city": "New York"}
for key, value in person.items():
    print(f"{key}: {value}")

person = {"name": "John", "age": 30, "city": "New York"}
for key in person.keys():
    print(key)

person = {"name": "John", "age": 30, "city": "New York"}
for value in person.values():
    print(value)

count = 0
while count < 5:
    print(count)
    count = count + 1

numbers = [1, 2, 3, 4, 5]
while numbers:
    print(numbers.pop())

correct_password = "python123"
password = ""
while password != correct_password:
    password = input("请输入密码: ")
    if password != correct_password:
        print("密码错误，请重新输入。")

print("密码正确，登录成功！")


def divide_numbers(a, b):
    if b == 0:
        raise ZeroDivisionError("除数不能为零。")
    return a / b


try:
    num1 = float(input("请输入被除数: "))
    num2 = float(input("请输入除数: "))
    result = divide_numbers(num1, num2)
    print(f"结果是: {result}")
except ValueError:
    print("输入无效，请输入有效的数字。")
except ZeroDivisionError as e:
    print(e)

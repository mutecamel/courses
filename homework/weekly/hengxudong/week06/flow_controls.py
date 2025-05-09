fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    fruit += ",ok"
    print(fruit)

message = "Hello"
for char in message:
    print(char)

for i in range(5):  # 01234
    print(i)

student = {"name": "Alice", "age": 20, "grade": "A"}
for key in student:
    print(key)

student = {"name": "Alice", "age": 20, "grade": "A"}
for key, value in student.items():
    print(f"{key}: {value}")

count = 0
while count < 5:
    print(count)
    count = count + 1

sum_num = 0
i = 1
while i <= 10:
    sum_num = sum_num + i
    i = i + 1
print("1 到 10 的整数之和为", sum_num)


numbers = [1, 2, 3, 4, 5]
while numbers:
    current_num = numbers.pop(0)
    print("当前处理的数字是:", current_num)

user_input = ""
while user_input != "quit":
    user_input = input("请输入内容（输入 quit 退出）: ")
    if user_input != "quit":
        print("你输入的是:", user_input)

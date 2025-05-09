fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    fruit += ", ok"
    print(fruit)

message = "Hello"
for char in message:
    print(char)

for i in range(5):
    print(i)

person = {"name": "John", "age": 30, "city": "New York"}
for key in person:
    print(key, ":", person[key])

count = 0
while count < 5:
    print(count)
    count = count + 1

numbers = [1, 2, 3, 4, 5]
while numbers:
    print(numbers.pop())

while True:
    try:
        user_input = input("请输入一个 1 到 10 之间的整数: ")
        number = int(user_input)
        if 1 <= number <= 10:
            print(f"你输入的有效数字是: {number}")
            break
        else:
            print("输入的数字不在 1 到 10 之间，请重新输入。")
    except ValueError:
        print("输入无效，请输入一个整数。")

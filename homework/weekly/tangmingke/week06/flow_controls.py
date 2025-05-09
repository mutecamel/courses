fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    fruit += ", ok"
    print(fruit)

word = "hello"
for char in word:
    print(char)

for i in range(5):
    print(i)

person = {"name": "John", "age": 30, "city": "New York"}
for key, value in person.items():
    print(f"{key}: {value}")

for i in range(3):
    for j in range(2):
        print(f"({i}, {j})")

i = 0
while i < 5:
    print(i)
    i = i + 1

user_input = ""
while user_input != "quit":
    user_input = input("请输入内容，输入 'quit' 退出: ")
    if user_input != "quit":
        print(f"你输入的是: {user_input}")

numbers = [1, 2, 3, 4, 5]
while numbers:
    number = numbers.pop(0)
    print(number)

total = 0
i = 1
while i <= 10:
    total = total + i
    i = i + 1
print(f"1 到 10 的和是: {total}")
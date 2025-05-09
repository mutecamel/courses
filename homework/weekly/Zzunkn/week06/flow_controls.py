fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    fruit = fruit + ",okk"
    print(fruit)

message = "Hello"
for char in message:
    print(char)

numbers = (1, 2, 3, 4, 5)
for num in numbers:
    print(num)

student = {"name": "Alice", "age": 20, "city": "New York"}
for key in student:
    print(key, ":", student[key])

count = 1
while count <= 5:
    print(count)
    count = count + 1

my_list = [10, 20, 30, 40]
while my_list:
    removed_item = my_list.pop()
    print(f"Removed {removed_item}, remaining list: {my_list}")

valid_input = False
while not valid_input:
    user_input = input("Please enter a number greater than 10: ")
    try:
        number = int(user_input)
        if number > 10:
            print("Valid input!")
            valid_input = True
        else:
            print("The number should be greater than 10. Try again.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

while True:
    try:
        user_input = input("请输入一个正整数: ")
        num = int(user_input)
        if num <= 0:
            raise ValueError("输入必须是正整数")
        print(f"你输入的正整数是: {num}")
        break
    except ValueError as e:
        print(f"输入无效: {e}，请重新输入。")

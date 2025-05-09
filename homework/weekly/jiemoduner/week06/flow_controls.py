fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    fruit = fruit + ", ok"
    print(fruit)


message = "Hello"
for char in message:
    print(char)

for i in range(5):
    print(i)


person = {'name': 'Alice', 'age': 25, 'city': 'New York'}
for key, value in person.items():
    print(f"{key}: {value}")


for i in range(3):
    for j in range(2):
        print(f"({i}, {j})")


count = 0
while count < 5:
    print(count)
    count = count + 1


numbers = [1, 2, 3, 4, 5]
while numbers:
    print(numbers.pop())


valid_input = False
while not valid_input:
    user_input = input("请输入一个大于 10 的数字: ")
    try:
        num = int(user_input)
        if num > 10:
            valid_input = True
            print("输入有效！")
        else:
            print("输入的数字不大于 10，请重新输入。")
    except ValueError:
        print("输入不是有效的数字，请重新输入。")
    

while True:
    user_choice = input("输入 'q' 退出: ")
    if user_choice == 'q':
        break
    print("你输入的不是 'q'，请继续。")
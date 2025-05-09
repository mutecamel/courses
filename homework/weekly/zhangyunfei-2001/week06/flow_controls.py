fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    fruit = fruit + ",okk"
    print(fruit)

message = "Hello"
for char in message:
    print(char)

person = {"name": "John", "age": 30, "city": "New York"}
# 遍历字典的键
for key in person:
    print(key)

# 遍历字典的值
for value in person.values():
    print(value)

# 遍历字典的键值对
for key, value in person.items():
    print(key, ":", value)

# 打印 0 到 4 的数字
for i in range(5):
    print(i)

# 打印 2 到 6 的数字
for i in range(2, 7):
    print(i)

# 打印 2 到 10 之间的偶数
for i in range(2, 11, 2):
    print(i)

numbers = (1, 2, 3, 4, 5)
for num in numbers:
    print(num)

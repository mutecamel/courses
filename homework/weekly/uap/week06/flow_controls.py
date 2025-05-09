fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

message = "Hello"
for char in message:
    print(char)

for i in range(5):
    print(i)

person = {"name": "John", "age": 30, "city": "New York"}
for key, value in person.items():
    print(f"{key}: {value}")

# while 条件循环
print("while 循环示例:")
count = 0
while count < 5:
    print(count)
    count += 1

# break 打断跳出循环
print("\nbreak 示例:")
count = 0
while True:
    if count == 3:
        break
    print(count)
    count += 1

# continue 跳至下一轮循环
print("\ncontinue 示例:")
for i in range(5):
    if i == 2:
        continue
    print(i)

# for...else 循环未被打断的处理
print("\nfor...else 示例:")
for i in range(5):
    print(i)
else:
    print("循环正常结束，未被 break 打断")

# if 条件分支
print("\nif 条件分支示例:")
num = 10
if num > 5:
    print("数字大于 5")

# if...elif...else 多重条件分支
print("\nif...elif...else 多重条件分支示例:")
num = 20
if num < 10:
    print("数字小于 10")
elif num < 20:
    print("数字小于 20 但大于等于 10")
else:
    print("数字大于等于 20")

# try...except...else...finally 捕捉异常的处理
print("\ntry...except...else...finally 示例:")
try:
    result = 10 / 0
except ZeroDivisionError:
    print("错误: 除数不能为零")
else:
    print("没有发生异常，结果是:", result)
finally:
    print("无论是否发生异常，此代码块都会执行")

# raise 主动抛出异常
print("\nraise 主动抛出异常示例:")


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("除数不能为零")
    return a / b


try:
    result = divide(10, 0)
except ZeroDivisionError as e:
    print("发生异常:", e)

# for 迭代循环 (iteration loop)
print("for 迭代循环示例：")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    fruit = fruit + ", ok"  # fruit += ", ok"
    print(fruit)

# 创建一个字典，存储学生的成绩信息
print("\nfor 字典循环实例：")
student_scores = {"Alice": 85, "Bob": 90, "Charlie": 78}
# 使用 for 循环遍历字典的键
for name in student_scores:
    print(f"{name}: {student_scores[name]}")

# while 条件循环 (conditional loop)
print("\nwhile 条件循环示例：")
count = 0
while count < 3:
    print(count)
    count = count + 1

# break 打断跳出循环
print("\nbreak 打断跳出循环示例：")
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num == 3:
        break
    print(num)

# continue 跳至下一轮循环
print("\ncontinue 跳至下一轮循环示例：")
for num in numbers:
    if num == 3:
        continue
    print(num)

# for...else 循环未被打断的处理
print("\nfor...else 循环未被打断的处理示例：")
for num in numbers:
    if num == 6:
        break
else:
    print("循环未被 break 打断")

# if 条件分支
print("\nif 条件分支示例：")
x = 10
if x > 5:
    print("x 大于 5")

# if...elif[...elif] 多重条件分支
print("\nif...elif 多重条件分支示例：")
y = 20
if y < 10:
    print("y 小于 10")
elif y < 25:
    print("y 小于 25 但不小于 10")
else:
    print("y 大于等于 25")

# if...else 未满足条件的处理
print("\nif...else 未满足条件的处理示例：")
z = 3
if z > 5:
    print("z 大于 5")
else:
    print("z 小于等于 5")

# try...except[...except...else...finally] 捕捉异常的处理
print("\ntry...except 捕捉异常的处理示例：")
try:
    result = 1 / 0
except ZeroDivisionError:
    print("发生了除零错误")
else:
    print("没有发生异常")
finally:
    print("无论是否发生异常，finally 块都会执行")

# raise 主动抛出异常
print("\nraise 主动抛出异常示例：")


def check_age(age):
    if age < 0:
        raise ValueError("年龄不能为负数")
    return age


try:
    age = check_age(-5)
except ValueError as e:
    print(e)

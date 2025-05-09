print("for 迭代循环 (iteration loop)举例：")
# 1. 遍历列表
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    fruit += " is good"
    print(fruit)

# 2. 遍历字符串
for char in "hello":
    print(char)  # 输出每个字符

# 3. 结合 range() 的固定次数循环
for i in range(3):
    print(i)  # 0, 1, 2

# 4. 遍历字典的键值对
person = {"name": "Alice", "age": 25}
for key in person.keys():
    print(key)

person = {"name": "Alice", "age": 25}
for value in person.values():
    print(value)

    person = {"name": "Alice", "age": 25}
for key, value in person.items():
    print(f"{key}: {value}")  # f-string 的真正价值在于动态嵌入变量或表达式


print("while 条件循环 (conditional loop)举例：")
# 1. 基本用法：条件为真时循环
count = 0
while count < 3:
    print(f"Count: {count}")  # 输出 0, 1, 2
    count += 1

# 2. 带 break 的循环（打断跳出循环）
while True:
    user_input = input("输入 'q' 退出: ")
    if user_input == "q":
        break  # 中断循环
    print(f"你输入了: {user_input}")

# 3. 带 continue 的循环（跳至下一轮循环）
num = 0
while num < 5:
    num += 1
    if num == 3:
        continue  # 跳过 3
    print(num)  # 输出 1, 2, 4, 5

# 4. 结合 else（循环正常结束时执行）
n = 0
while n < 3:
    print(n)  # 输出 0, 1, 2
    n += 1
else:
    print("循环完成！")


numbers = [1, 3, 5, 7]
target = 4
for num in numbers:
    if num == target:
        print("找到目标！")
        break
else:
    print("未找到目标！")  # 因为循环未被 break 中断

# if 条件分支
day = "周三"
if day == "周一":
    print("上班")
elif day == "周二":
    print("继续上班")
elif day == "周三":
    print("摸鱼")  # 输出：摸鱼
elif day == "周四":
    print("快周末了")
else:
    print("休息日")

# 异常处理
# try...except捕捉异常的处理
try:
    num = int(input("请输入数字: "))  # 可能出错的地方
    result = 10 / num  # 可能出错的地方
    print(f"结果是: {result}")
except ValueError:
    print("错误：请输入有效数字！")
except ZeroDivisionError:
    print("错误：不能除以0！")
else:
    print("计算成功！")  # 没有错误时执行
finally:
    print("程序结束")  # 无论是否有错都会执行

# raise主动抛出异常
age = int(input("请输入年龄: "))
if age < 0:
    raise ValueError("年龄不能小于0！")
elif age < 18:
    print("未成年")
else:
    print("成年")

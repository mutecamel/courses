#  for 语句

fruits = ["苹果", "香蕉", "橙子"]
for fruit in fruits:
    fruit += fruit + ", delicious"
    print(fruit)  #   苹果苹果, delicious
    fruit += ", healthy"
    print(fruit)  #   苹果苹果, delicious, healthy

word = "Beauty, Clever, Independent"
for char in word:
    print(char)

for i in range(100):  # 生成 0 到 100 的数字
    print(i)  #   0 1 2 3 ... 99

for i in range(44):
    for j in range(21):
        print(f"i = {i}, j = {j}")

numbers = [1, 2, 3, 4, 5, 9]
total = 20
for num in numbers:
    total += num
print(f"总和: {total}")  #   总和: 44

girl = {"food": "meet", "vegetable": "cherry", "city": "harbin"}
for key, value in girl.items():
    print(f"{key}: {value}")

girl = {"food": "meet", "vegetable": "cherry", "city": "harbin"}
for key in girl.keys():
    print(f"{key}: {value}")  #   food: harbin

girl = {"food": "meet", "vegetable": "cherry", "city": "harbin"}
for key in girl.keys():
    print(key)

girl = {"food": "meet", "vegetable": "cherry", "city": "harbin"}
for value in girl.values():
    print(value)

# while条件循环语句

count = 29
while count < 50:
    print(count)
    count += 3  # 29 32 35 38 41 44 47

numbers = [1, 2, 3, 4, 5]
while numbers:
    print(numbers.pop())  # 54321

i = 1
while i <= 3:
    j = 1
    while j <= 2:
        print(f"i = {i}, j = {j}")
        j += 1
    i += 1

numbers = [1, 2, 3, 4, 5]
print(len(numbers))  #   5
total = 0
index = 0
while index < len(numbers):
    total += numbers[index]
    index += 1
print(f"总和: {total}")  #  总和: 15

# break continue

for i in range(10):
    if i % 2 == 0:
        print(f"{i} 是偶数，跳过当前循环...")
        continue  # 跳过偶数，进入下一轮循环
    print(f"{i} 是奇数，继续处理...")
    if i > 5:
        print(f"{i} 大于 5, 跳出循环...")
        break  # 跳出循环

#  for...else 循环未被打断的处理

numbers = [1, 2, 3, 4, 5]

for num in numbers:
    print(f"当前数字：{num}")
    # 如果找到某个条件，就 break
    if num == 6:
        print("找到 6, 跳出循环")
        break
else:
    print("循环正常结束，没有被 break 打断")

numbers = [1, 2, 3, 4, 5, 6, 7]

for num in numbers:
    print(f"当前数字：{num}")
    # 如果找到某个条件，就 break
    if num >= 6:
        print("找到大于 6, 跳出循环")
        break
else:
    print("循环正常结束，没有被 break 打断")

target = 6
numbers = [1, 2, 3, 4, 5]

for num in numbers:
    print(f"检查数字：{num}")
    if num == target:
        print(f"找到目标数字：{target}")
        break
else:
    print(f"未找到目标数字：{target}")

target = 6
numbers = [3, 4, 5, 6, 7, 9, 10]

for num in numbers:
    print(f"检查数字：{num}")
    if num == target:
        print(f"找到目标数字：{target}")
        break
else:
    print(f"未找到目标数字：{target}")

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
target = 5

for row in matrix:
    for num in row:
        print(f"检查数字：{num}")
        if num == target:
            print(f"找到目标数字：{target}")
            break
    else:
        continue
    break
else:
    print(f"未找到目标数字：{target}")

#   if...elif[...elif] 多重条件分支

score = int(input("请输入你的分数(0-100):"))

if score >= 90:
    print("成绩等级:A")
elif score >= 80:
    print("成绩等级:B")
elif score >= 70:
    print("成绩等级:C")
elif score >= 60:
    print("成绩等级:D")
else:
    print("成绩等级:F")

#  if...else 未满足条件的处理

number = 6888

if number > 5:
    print(f"{number} 大于 5")
else:
    print(f"{number} 不大于 5")

#  try...except[...except...else...finally] 捕捉异常的处理


def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("错误：除数不能为零！")
    except TypeError:
        print("错误：输入的参数类型不正确！")
    else:
        print(f"除法运算成功，结果为：{result}")
    finally:
        print("无论是否发生异常，都会执行 finally 块。")


# 测试 1：正常情况
print("测试 1:正常情况")
divide_numbers(10, 2)

# 测试 2：除数为零
print("\n测试 2:除数为零")
divide_numbers(10, 0)

# 测试 3：输入类型错误
print("\n测试 3:输入类型错误")
divide_numbers(10, "2")

#  raise 主动抛出异常


class NegativeNumberError(Exception):
    def __init__(self, message="输入的数字不能为负数！"):
        self.message = message
        super().__init__(self.message)


def validate_number(number):
    if number < 0:
        raise NegativeNumberError
    return number


def main():
    try:
        # 测试 1：正常情况
        print("测试 1:正常情况")
        num = validate_number(5)
        print(f"验证通过，数字为：{num}")

        # 测试 2：抛出异常
        print("\n测试 2:抛出异常")
        num = validate_number(-3)
        print(f"验证通过，数字为：{num}")
    except NegativeNumberError as e:
        print(f"捕获到自定义异常：{e}")


if __name__ == "__main__":
    main()

# 语句结合


def validate_age(age):
    """
    验证年龄是否在合理范围内。
    如果年龄小于0或大于120,抛出异常。
    """
    if age < 0:
        raise ValueError("年龄不能为负数！")
    elif age > 120:
        raise ValueError("年龄不能超过120岁!")
    return age


def main():
    try:
        # 测试 1：正常情况
        print("测试 1:正常情况")
        age = validate_age(25)
        print(f"验证通过，年龄为：{age}")

        # 测试 2：年龄为负数
        print("\n测试 2:年龄为负数")
        age = validate_age(-5)
        print(f"验证通过，年龄为：{age}")

        # 测试 3：年龄超过120
        print("\n测试 3:年龄超过120")
        age = validate_age(150)
        print(f"验证通过，年龄为：{age}")
    except ValueError as e:
        print(f"捕获到异常：{e}")


if __name__ == "__main__":
    main()

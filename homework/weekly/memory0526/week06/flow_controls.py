##for语句的学习：in之后的对象必须要可以迭代
# 遍历列表
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    fruit = fruit + ",OK"
    print(fruit)
# 输出：
# apple
# banana
# cherry


##遍历字符串中的字符
text = "Seven"
for char in text:
    print(char)
# 输出：
# H
# e
# l
# l
# o

##range函数的使用，控制循环的次数
# 循环 5 次（0到4）
for i in range(5):
    print(i)  # 输出：0,1,2,3,4

# 指定起始和结束值
for i in range(2, 6):
    print(i)  # 输出：2,3,4,5

# 指定步长
for i in range(0, 10, 2):
    print(i)  # 输出：0,2,4,6,8


##遍历字典
person = {"name": "Alice", "age": 30, "city": "Paris"}
# 遍历键
for key in person.keys():
    print(key)  # 输出：name, age, city

# 遍历值
person = {"name": "Alice", "age": 30, "city": "Paris"}
for value in person.values():
    print(value)

# 遍历键值对
person = {"name": "Alice", "age": 30, "city": "Paris"}
for key, value in person.items():
    print(f"{key}: {value}")

##while语句学习
##基础计数循环
count = 0
while count < 3:
    print(f"当前计数: {count}")
    count += 1


##处理表格，while后面可以接任何对象
numbers = [3, 1, 4, 1, 5, 9, 2]
while numbers:  # 列表不为空时循环
    current = numbers.pop(0)  ##pop为number的内置函数单出列表中的数字
    if current == 5:
        print("找到 5，停止处理")
        break
    print(f"处理数字: {current}")

##for else的语句使用：验证列表是否全满足条件
primes = [2, 3, 5, 7, 11]
for p in primes:
    if p % 2 == 0 and p != 2:  # 检查是否所有质数都是奇数（除了2）
        print(f"{p} 不是奇数质数")
        break
else:
    print("所有质数都符合条件")  # 会被执行


##复杂一点的完整异常处理结构
def validate_age(age_str):
    """
    验证年龄是否有效
    - 必须为数字且 >= 0
    - 若无效则主动抛出 ValueError 异常
    """
    if not age_str.isdigit():
        # 手动抛出异常（非数字）
        raise ValueError("年龄必须为数字")
    age = int(age_str)
    if age < 0:
        # 手动抛出异常（负数）
        raise ValueError("年龄不能为负数")
    return age


# 主程序
try:
    user_input = input("请输入您的年龄: ")
    age = validate_age(user_input)  # 可能触发异常的调用

except ValueError as ve:
    # 捕获 ValueError 异常（具体错误）
    print(f"输入错误: {ve}")

except Exception as e:
    # 捕获其他所有未处理的异常（兜底处理）
    print(f"未知错误: {e}")

else:
    # 仅当 try 块无异常时执行
    print(f"验证成功！您的年龄是 {age} 岁")

finally:
    # 无论是否异常都会执行（清理资源）
    print("程序执行结束（finally 块）")

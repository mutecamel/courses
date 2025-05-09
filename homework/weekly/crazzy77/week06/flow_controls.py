fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    fruit += ".ok"
    print(fruit)

message = "Hello"
for char in message:
    print(char)

numbers = (1, 2, 3, 4, 5)
for num in numbers:
    print(num * 2)

for i in range(5):
    print(i)

student = {"name": "Alice", "age": 20, "major": "Computer Science"}

# 遍历字典的键
for key in student:
    print(key)

# 遍历字典的值
for value in student.values():
    print(value)

# 同时遍历字典的键和值
for key, value in student.items():
    print(f"{key}: {value}")

count = 0
while count < 5:
    print(count)
    count = count + 1

valid_input = False
while not valid_input:
    user_input = input("请输入一个大于 10 的整数: ")
    try:
        num = int(user_input)
        if num > 10:
            valid_input = True
            print("输入有效，你输入的数字是:", num)
        else:
            print("输入无效，请输入一个大于 10 的整数。")
    except ValueError:
        print("输入无效，请输入一个有效的整数。")

while True:
    user_input = input("请输入一个数字（输入 q 退出）: ")
    if user_input == "q":
        break
    try:
        num = int(user_input)
        print(f"你输入的数字是 {num}")
    except ValueError:
        print("输入无效，请输入一个数字或 q。")

# 获取玩家的得分
score = int(input("请输入你的游戏得分: "))

# 综合运用条件判断
if score < 0:
    print("得分无效，得分不能为负数。")
elif score < 30:
    print("你的得分较低，继续加油哦！没有奖励。")
elif score < 60:
    print("你的表现一般，奖励你一个小徽章。")
elif score < 80:
    print("你表现得不错，奖励你一个精美钥匙链。")
elif score < 100:
    print("你太厉害了，奖励你一张游戏点卡。")
elif score == 100:
    print("满分！超级厉害，奖励你一台游戏机。")
else:
    print("得分无效，满分是 100 分。")

try:
    num1 = int(input("请输入被除数: "))
    num2 = int(input("请输入除数: "))
    result = num1 / num2
    print(f"结果是: {result}")
except ValueError:
    print("输入无效，请输入有效的整数。")
except ZeroDivisionError:
    print("除数不能为零。")
else:
    print("运算成功完成。")
finally:
    print("程序结束。")


class NegativeNumberError(Exception):
    pass


def calculate_square_root(num):
    if num < 0:
        raise NegativeNumberError("不能计算负数的平方根。")
    return num**0.5


try:
    result = calculate_square_root(-4)
    print(result)
except NegativeNumberError as e:
    print(f"捕获到异常: {e}")

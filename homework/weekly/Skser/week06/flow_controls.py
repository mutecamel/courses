# 打印乘法表 for语句
print("乘法表:")
for i in range(1, 10):  # 1到9
    for j in range(1, i + 1):
        print(f"{j}×{i}={i * j}", end="\t")
    print()  # 换行

# 猜数字游戏 while语句
import random

target = random.randint(1, 100)
guess = -1
print("猜数字游戏(1-100):")
while guess != target:
    guess = int(input("请输入你的猜测: "))
    if guess < target:
        print("猜小了!")
    elif guess > target:
        print("猜大了!")
print("恭喜你猜对了!")

# 寻找第一个能被7和9整除的数  break语句
print("寻找第一个能被7和9整除的数:")
for num in range(1, 1000):
    if num % 7 == 0 and num % 9 == 0:
        print(f"找到: {num}")
        break  # 找到后立即退出循环

# 打印1-10的奇数  continue语句
print("1-10的奇数:")
for i in range(1, 11):
    if i % 2 == 0:
        continue  # 跳过偶数
    print(i, end=" ")
print()

# 检查质数  for……else语句
num = 13
print(f"检查{num}是否是质数:")
for i in range(2, int(num**0.5) + 1):
    if num % i == 0:
        print(f"{num}不是质数")
        break
else:  # 循环正常结束(未被打断)时执行
    print(f"{num}是质数")

# 年龄判断 if语句
age = 18
print("年龄判断:")
if age >= 18:
    print("你已成年!")

# 成绩等级评定  if……elif语句
score = 85
print("成绩等级评定:")
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("E")

# 奇偶数判断 if……else语句
num = 7
print("奇偶数判断:")
if num % 2 == 0:
    print(f"{num}是偶数")
else:
    print(f"{num}是奇数")

# 安全除法计算 try……except语句
print("安全除法计算:")
while True:
    try:
        a = float(input("请输入被除数: "))
        b = float(input("请输入除数: "))
        result = a / b
    except ValueError:
        print("错误: 请输入数字!")
    except ZeroDivisionError:
        print("错误: 除数不能为零!")
    else:
        print(f"结果为: {result:.2f}")
        break
    finally:
        print("--- 尝试完成 ---")


# 验证密码强度  raise语句
def check_password(password):
    if len(password) < 8:
        raise ValueError("密码长度至少8位")
    if not any(c.isdigit() for c in password):
        raise ValueError("密码必须包含数字")
    if not any(c.isupper() for c in password):
        raise ValueError("密码必须包含大写字母")
    return True


print("密码强度检查:")
try:
    pwd = input("请输入密码: ")
    if check_password(pwd):
        print("密码强度合格!")
except ValueError as e:
    print(f"密码不合格: {e}")

# for 迭代循环
print("for 迭代循环示例：")
for i in range(1, 6):
    print(i)

# while 条件循环
print("\nwhile 条件循环示例：")
count = 1
while count <= 3:
    print(count)
    count += 1

# break 打断循环
print("\nbreak 示例：")
for num in range(1, 11):
    if num == 5:
        break
    print(num)

# continue 跳至下一轮循环
print("\ncontinue 示例：")
for num in range(1, 6):
    if num % 2 == 0:
        continue
    print(num)

# for...else 循环未被打断的处理
print("\nfor...else 示例：")
for i in range(1, 4):
    print(i)
else:
    print("for 循环正常结束（未被 break）")

# if 条件分支
print("\nif 条件分支示例：")
x = 7
if x > 5:
    print("x 大于 5")

# if...elif...else 多重条件分支
print("\nif...elif...else 示例：")
score = 85
if score >= 90:
    print("优秀")
elif score >= 80:
    print("良好")
else:
    print("中等")

# try...except...finally 捕捉异常的处理
print("\ntry...except...finally 示例：")
try:
    num = int("abc")
except ValueError:
    print("输入不是有效数字")
finally:
    print("无论是否异常，finally 都会执行")

# raise 主动抛出异常
print("\nraise 示例：")
age = -5
if age < 0:
    raise ValueError("年龄不能为负数")
# for 迭代循环 (iteration loop)
# for循环用于对可迭代对象（如列表、元组、字符串等）进行遍历。
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# while 条件循环 (conditional loop)
# hile循环会在条件为真时持续执行，直到条件变为假。
count = 0
while count < 3:
    print(count)
    count = count + 1

# break 打断跳出循环
# break语句用于在循环内部提前终止循环，即使循环条件依然为真。
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    if fruit == "banana":
        break
    print(fruit)

# continue 跳至下一轮循环
# continue语句用于跳过当前循环的剩余部分，直接进入下一轮循环。
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    if fruit == "banana":
        continue
    print(fruit)

# for...else 循环未被打断的处理
# 在for循环后添加else语句，当循环没有被break语句中断时，else块中的代码会被执行。
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
else:
    print("No break occurred.")

# if 条件分支
# if语句依据条件判断结果决定是否执行特定代码块。
x = 10
if x > 5:
    print("x is greater than 5")

# if...elif [...elif] 多重条件分支
# if...elif语句用于对多个条件进行判断，当if条件不满足时，会依次检查elif条件。
x = 10
if x < 0:
    print("x is negative")
elif x == 0:
    print("x is zero")
elif x > 0:
    print("x is positive")

# if...else 未满足条件的处理
# if...else语句用于在条件为真时执行一个代码块，条件为假时执行另一个代码块。
x = 10
if x > 20:
    print("x is greater than 20")
else:
    print("x is less than or equal to 20")

# try...except [...except...else...finally] 捕捉异常的处理
# try...except语句用于捕获并处理代码块中可能出现的异常。else块在try块没有抛出异常时执行，finally块无论是否有异常都会执行。
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: division by zero")
else:
    print("No error occurred.")
finally:
    print("This is the finally block.")

# raise 主动抛出异常
# raise语句用于主动抛出异常。
x = -1
if x < 0:
    raise ValueError("x cannot be negative")

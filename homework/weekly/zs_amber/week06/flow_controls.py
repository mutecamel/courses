fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

    message = "Hello"
for char in message:
    print(char)

numbers = (1, 2, 3, 4, 5)
for num in numbers:
    print(num)
person = {"name": "John", "age": 30, "city": "New York"}
# 遍历字典的键
for key in person:
    print(key)

count = 0
while count < 5:
    print(count)
    count = count + 1


# 定义一个自定义异常类
class NegativeNumberError(Exception):
    def __init__(self, message="输入的数字不能为负数"):
        self.message = message
        super().__init__(self.message)


def square_root(num):
    try:
        if num < 0:
            # 主动抛出自定义异常
            raise NegativeNumberError()
        return num**0.5
    except NegativeNumberError as e:
        print(f"错误: {e.message}")


# 测试函数
result1 = square_root(9)
print(f"9 的平方根是: {result1}")

result2 = square_root(-4)

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    fruit = fruit + ", ok"
    print(fruit)


message = "Hello"
for char in message:
    print(char)

for i in range(5):
    print(i)

person = {"name": "John", "age": 30, "city": "New York"}
for key in person.keys():
    print(f"{key}:")

count = 1
while count <= 5:
    print(count)
    count = count + 1

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
while numbers:
    num = numbers.pop(0)
    if num % 2 != 0:
        numbers.append(num)

print(numbers)


def calculate_average(num_list):
    try:
        if not num_list:
            # 若列表为空，抛出异常
            raise ValueError("输入的列表为空，无法计算平均值。")
        total = sum(num_list)
        return total / len(num_list)
    except ValueError as e:
        print(e)
        return None


numbers = []
average = calculate_average(numbers)
if average is not None:
    print(f"平均值是: {average}")


def calculate_average(num_list):
    try:
        if not num_list:
            # 若列表为空，抛出异常
            raise ValueError("输入的列表为空，无法计算平均值。")
        total = sum(num_list)
        return total / len(num_list)
    except ValueError as e:
        print(e)
        return None


numbers = []
average = calculate_average(numbers)
if average is not None:
    print(f"平均值是: {average}")


class CustomError(Exception):
    pass


def inner_function():
    try:
        # 主动抛出异常
        raise CustomError("这是一个自定义异常。")
    except CustomError as e:
        print(f"在内部函数中捕获到异常: {e}")
        # 重新抛出异常
        raise


def outer_function():
    try:
        inner_function()
    except CustomError as e:
        print(f"在外部函数中捕获到重新抛出的异常: {e}")


outer_function()

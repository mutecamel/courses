count = 0
while count < 5:
    print(count)
    count = count + 1


sum_num = 0
i = 1
while i <= 10:
    sum_num = sum_num + i
    i = i + 1
print("1 到 10 的整数之和为", sum_num)

my_list = [1, 2, 3, 4, 5]
index = 0
while index < len(my_list):
    print(my_list[index])
    index = index + 1

number = 0
while number <= 10:
    try:
        number = int(input("请输入一个大于 10 的数字: "))
    except ValueError:
        print("输入无效，请输入一个整数。")

print("你输入的有效数字是:", number)

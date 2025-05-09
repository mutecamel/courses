"""
fruits = [
    "apple",
    "banana",
    "cherry",
]  # 遍历列表,在这个例子中，for 循环遍历了 fruits 列表，每次循环时，fruit 变量会依次被赋值为列表中的元素，并将其打印出来。
for fruit in fruits:
    fruit = fruit + ", like"
    print(fruit)

message = "Hello"  # 遍历字符串,此例中，for 循环遍历了字符串 "Hello"，char 变量会依次取到字符串中的每个字符并打印。
for char in message:
    print(char)

for i in range(
    5
):  # 使用 range() 函数遍历数字序列,range(5) 会生成一个从 0 到 4 的数字序列，for 循环会依次将这些数字赋值给 i 并打印。
    print(i)

student = {
    "name": "John",
    "age": 20,
    "grade": "A",
}  # 遍历字典的键,在这个例子中，for 循环遍历了字典 student 的键，并将每个键打印出来。
for key in student:
    print(key)

student = {
    "name": "John",
    "age": 20,
    "grade": "A",
}  # 遍历字典的键值对,items() 方法会返回字典的键值对，for 循环会依次将键和值分别赋值给 key 和 value，并打印出来。
for key, value in student.items():
    print(f"{key}: {value}")

for i in range(
    3
):  # 嵌套 for 循环,这个例子展示了嵌套 for 循环的使用。外层循环控制 i 的值，内层循环控制 j 的值，每次内层循环结束后，外层循环才会进入下一次迭代。
    for j in range(2):
        print(f"({i}, {j})")"""

"""count = 0
while count < 5:
    print(count)
    count = count + 1"""

"""number = 0
while number != 10:
    number = int(input("请输入一个数字（输入 10 结束）: "))
print("你输入了 10，循环结束。")"""

# 定义一个包含整数的列表
"""numbers = [1, 2, 3, 4, 5]
# 初始化索引变量，用于遍历列表
index = 0
# 初始化总和变量，用于存储累加的结果
sum_result = 0
# 当索引小于列表的长度时，执行循环体
while index < len(numbers):
    # 将当前索引对应的列表元素累加到总和中
    sum_result = sum_result + numbers[index]
    # 索引加 1，以便访问下一个元素
    index = index + 1
# 循环结束后，打印列表元素的总和
print("列表元素的和为:", sum_result)"""

# 模拟一个简单的游戏场景，有多个关卡和不同的道具，玩家需要通过完成任务来通关

# 定义关卡列表，每个关卡有不同的任务要求和奖励
levels = [
    {"name": "新手关卡", "requirement": 3, "reward": "初级钥匙"},
    {"name": "中级关卡", "requirement": 6, "reward": "中级钥匙"},
    {"name": "高级关卡", "requirement": 9, "reward": "高级钥匙"},
]

# 玩家初始得分
player_score = 0
# 玩家初始拥有的钥匙
player_keys = []

# 外层 while 条件循环，用于控制游戏是否继续进行
while True:
    print("\n当前游戏状态：")
    print(f"玩家得分: {player_score}")
    print(f"玩家拥有的钥匙: {player_keys}")

    # for 迭代循环，遍历每个关卡
    for level in levels:
        print(f"\n当前关卡: {level['name']}")
        print(f"本关卡任务要求得分达到: {level['requirement']}")

        # 内层 while 条件循环，用于在当前关卡中尝试完成任务
        while player_score < level["requirement"]:
            try:
                # 提示玩家输入本次行动获得的得分，使用 try...except 捕捉异常
                score_earned = int(
                    input("请输入本次行动获得的得分 (输入非数字将报错): ")
                )
                if score_earned < 0:
                    # 主动抛出异常，如果得分是负数
                    raise ValueError("得分不能为负数！")
                player_score += score_earned
                print(f"当前得分已更新为: {player_score}")
            except ValueError as e:
                print(f"输入错误: {e}，请重新输入有效的得分。")
                continue  # 跳至下一轮循环，重新让玩家输入得分

        print(f"恭喜你，通过了 {level['name']}！")
        player_keys.append(level["reward"])
        print(f"你获得了 {level['reward']}。")

        # 检查是否满足某个条件，使用 if 条件分支
        if len(player_keys) == len(levels):
            print("你已经通过了所有关卡，游戏胜利！")
            break  # 打断跳出循环，结束游戏

    else:
        # for...else 循环未被打断的处理
        print("你已经完成了当前所有可挑战的关卡，但还未通关全部。")

    # 询问玩家是否继续游戏，使用 if...else 未满足条件的处理
    play_again = input("\n是否继续游戏？(输入 'y' 继续，其他任意键退出): ")
    if play_again.lower() != "y":
        print("游戏结束，感谢游玩！")
        break  # 打断跳出循环，结束外层游戏循环

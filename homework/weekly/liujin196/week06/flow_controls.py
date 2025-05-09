# for 循环示例：打印 1 到 5
for i in range(1, 6):
    print(f"第 {i} 次循环")
# while 循环示例：打印 1 到 5
n = 1
while n <= 5:
    print(f"[while] 第 {n} 次循环")
    n += 1
# break 示例：打印 1 到 5，遇到 3 就中断
for i in range(1, 6):
    if i == 3:
        print("遇到 3，退出循环")
        break
    print(f"[break] 第 {i} 次循环")
# continue 示例：打印 1 到 5，遇到 3 就跳过
for i in range(1, 6):
    if i == 3:
        print("遇到 3，跳过本次循环")
        continue
    print(f"[continue] 第 {i} 次循环")
# for...else 示例：遍历列表，没遇到 break 就执行 else
for i in range(1, 6):
    print(f"[for...else] 正在检查数字：{i}")
    if i == 10:
        print("找到了 10！")
        break
else:
    print("[for...else] 没有找到 10，执行了 else 块")
# if...else 示例：判断奇偶
for i in range(1, 6):
    if i % 2 == 0:
        print(f"[if...else] {i} 是偶数")
    else:
        print(f"[if...else] {i} 是奇数")
# try...except 示例：捕获非数字输入
for i in range(3):
    try:
        x = int(input("[try...except] 请输入一个整数："))
        print(f"[try...except] 你输入的是：{x}")
    except ValueError:
        print("[try...except] 输入不是有效的整数！")
# raise 示例：遇到 3 主动抛出异常
for i in range(1, 6):
    print(f"[raise] 当前数字：{i}")
    if i == 3:
        raise ValueError("[raise] 我不喜欢 3，主动抛出异常！")

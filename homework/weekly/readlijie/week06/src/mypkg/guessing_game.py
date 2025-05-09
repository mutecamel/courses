import random


def guessing_game():
    # 生成 1 到 100 之间的随机整数
    secret_number = random.randint(1, 100)  # 赋值语句
    n = 0

    print("欢迎来到猜数字游戏！我已经想好了一个 1 到 100 之间的数字，你可以开始猜啦。")

    while True:
        n += 1
        # 获取玩家输入
        guess = input(
            f"(第 {n} 次尝试) 请输入你猜的数字 (输入整数, 或者输入 q 回车退出): "
        )
        guess = guess.strip()  # 去除多余空白字符

        if guess == "q":
            break

        try:
            guess = int(guess)
        except ValueError:
            print("输入无效🙅，请输入一个整数。")
            continue

        if guess < 1 or guess > 100:
            print("输入无效🙅，输入值应该在 1～100 之间。")
            continue

        if guess == secret_number:
            print("恭喜你🎉，猜对了！")
            break

        if guess < secret_number:
            print("猜的数字太小了，再试试⤴️。")
            continue

        if guess > secret_number:
            print("猜的数字太大了，再试试⤵️。")
            continue

        raise NotImplementedError  # 未实施异常

    print("游戏结束，再见👋。")


if __name__ == "__main__":
    guessing_game()

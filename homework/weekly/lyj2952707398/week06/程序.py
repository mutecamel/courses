# 1. environment.yml
yaml
name: week06
channels:
  - defaults
dependencies:
  - python=3.12
  - pip
  - pip:
    - -e .
# 2. guessing_game.py
import random

def guessing_game():
    secret_number = random.randint(1, 100)
    n = 0

    print("欢迎来到猜数字游戏！我已经想好了一个 1 到 100 之间的数字，你可以开始猜啦。")

    while True:
        n += 1
        guess = input(f"(第 {n} 次尝试) 请输入你猜的数字 (输入整数, 或者输入 q 回车退出): ").strip()

        if guess == "q":
            break
        
        try:
            guess = int(guess)
        except ValueError:
            print("输入无效🙅，请输入一个整数。")
            continue
        
        if not 1 <= guess <= 100:
            print("输入无效🙅，输入值应该在 1～100 之间。")
            continue
        
        if guess == secret_number:
            print("恭喜你🎉，猜对了！")
            break

        print("猜的数字太小了，再试试⤴️。" if guess < secret_number else "猜的数字太大了，再试试⤵️。")

    print("游戏结束，再见👋。")

if __name__ == "__main__":
    guessing_game()
# 3. flow_controls.py
# python
# For loop
print("For loop:")
for i in range(3):
    print(f"Iteration {i}")

# While loop
print("\nWhile loop:")
count = 0
while count < 3:
    print(count)
    count += 1

# Break example
print("\nBreak:")
for i in range(5):
    if i == 3:
        break
    print(i)

# Continue example
print("\nContinue:")
for i in range(5):
    if i % 2 == 0:
        continue
    print(i)

# For-else
print("\nFor-else:")
for i in range(3):
    print(i)
else:
    print("Loop completed normally")

# If-elif-else
print("\nIf-elif-else:")
x = 10
if x < 5:
    print("Small")
elif x < 15:
    print("Medium")
else:
    print("Large")

# Try-except
print("\nTry-except:")
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    print(result)
finally:
    print("Cleanup")

# Raise
print("\nRaise:")
try:
    raise ValueError("Custom error")
except ValueError as e:
    print(f"Caught error: {e}")
# 4. src/mypkg/mylib.py
# python
def func1():
    print("func1: No parameters, no return")

def func2():
    return "func2: No parameters, has return"

def func3(a):
    print(f"func3: Positional param: {a}")

def func4(b=10):
    print(f"func4: Named param: {b}")

def func5(a, b, c=0, d=0):
    print(f"func5: a={a}, b={b}, c={c}, d={d}")

def func6(a, /):
    print(f"func6: Positional-only: {a}")

def func7(*, a):
    print(f"func7: Keyword-only: {a}")

def func8(*args):
    print(f"func8: Varargs: {args}")

def func9(​**​kwargs):
    print(f"func9: Kwargs: {kwargs}")

def func10(a, b, c=0):
    print(f"func10: Unpacked args: a={a}, b={b}, c={c}")

def func11(a, b=0, c=0):
    print(f"func11: Unpacked kwargs: a={a}, b={b}, c={c}")

def func12(a: int, b: str) -> str:
    """Example function with type hints
    Args:
        a: Integer parameter
        b: String parameter
    Returns:
        Combined string
    """
    return f"{a}-{b}"
# 5. scripts/myjob.py
# python
from mypkg.mylib import *

func1()
print(func2())

func3(5)
func3(a=5)

func4()
func4(20)
func4(b=20)

func5(1, 2, d=4, c=3)
func5(1, 2, 3, d=4)

func6(5)
func7(a=5)

func8(1, 2, 3)
func9(a=1, b=2)

func10(*(1, 2), c=3)
func11(​**​{'a': 10, 'b': 20, 'c': 30})

print(func12(123, "test"))
# 6. pyproject.toml
# toml
[project]
name = "mypkg"
version = "0.1.0"
description = "My practice package"
authors = [{name = "Your Name", email = "you@example.com"}]

[build-system]
requires = ["setuptools>=42"]
build-backend = "setuptools.build_meta"
# 7. src/mypkg/init.py
python
from .mylib import *
# 项目结构
# .
# ├── environment.yml
# ├── pyproject.toml
# ├── src/
# │   └── mypkg/
# │       ├── __init__.py
# │       └── mylib.py
# └── scripts/
#     └── myjob.py
# 操作步骤
# # 创建conda环境
# bash
# conda env create -f environment.yml
# conda activate week06
# 安装本地包
# bash
# pip install -e .
# 运行测试脚本
# bash
# python scripts/myjob.py
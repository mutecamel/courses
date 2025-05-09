from pathlib import Path
from pprint import pprint

p = Path(".")  # 当前目录
print(p)
print(p.exists())
print(p.absolute())  # 绝对路径
print(list(p.iterdir()))  # 列举文件夹
pprint(list(p.iterdir()))

# 新建文件夹
p = Path("./data1")
print(p.exists())
p.mkdir(exist_ok=True)  # 创建文件夹 若目录已存在不会抛出异常
print(p.exists())
print(p.is_dir())

p = Path(".")
p2 = p / "readme.md"
print(p2)
p3 = p2.absolute()
print(p3)

from pathlib import Path
from pprint import pprint

p = Path(".")  # .代表当前目录
print(p)
print(p.exists())  # True
print(p.absolute())  # 绝对路径
pprint(list(p.iterdir()))  # 显示当前目录下有哪些文件

p = Path("./dokyeom")
print(p.exists())  # 检查文件夹dokyeom是否存在，结果为False，即不存在
p.mkdir(exist_ok=True)  # 创建文件夹
print(p.exists())  # 检查文件夹dokyeom是否存在，结果为True，即创建成功，文件夹存在
print(p.is_dir())  # 检测p是否是文件夹，结果为True

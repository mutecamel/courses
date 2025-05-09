from pathlib import Path
from pprint import pprint

# 获取当前路径并创建Path对象
p = Path('.')
# 打印当前路径
print(p)
# 检查当前路径是否存在
print(p.exists())
# 获取当前路径的绝对路径
print(p.absolute())
# 以美观的格式打印当前路径下的目录迭代器内容（即子目录和文件）
pprint(list(p.iterdir()))

# 获取当前路径下名为'data2'的子路径并创建Path对象
p = Path('./data2')
# 检查该路径是否存在
print(p.exists())
# 检查该路径是否为目录
print(p.is_dir())

# 获取当前路径
p = Path('.')
# 拼接当前路径和'README.txt'文件名，创建新的Path对象
p2 = p / 'README.txt'
# 获取p2的绝对路径
p3 = p2.absolute()
# 打印p2
print(p2)
# 打印p3
print(p3)

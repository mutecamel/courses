from pathlib import Path

p = Path(".")
print(p)
print(p.exists)
print(p.absolute())
print(list(p.iterdir()))

p = Path('.data1')
print(p.exists())
p.mkdir
print(p.exists())
print(p.is_dir())


# 创建一个 Path 对象
file_path = Path('test.txt')

# 获取文件的绝对路径
absolute_path = file_path.resolve()
print("绝对路径:", absolute_path)

# 获取路径中的目录部分
dir_name = absolute_path.parent
print("目录部分:", dir_name)

# 获取路径中的文件名部分
file_name = absolute_path.name
print("文件名部分:", file_name)

# 检查路径是否存在
path_exists = absolute_path.exists()
print("路径是否存在:", path_exists)

# 检查路径是否为文件
is_file = absolute_path.is_file()
print("是否为文件:", is_file)

# 检查路径是否为目录
is_dir = dir_name.is_dir()
print("是否为目录:", is_dir)

# 连接多个路径组件
new_path = dir_name / 'new_file.txt'
print("新路径:", new_path)

from pathlib import Path

a = Path(".")
print(a)
print(a.exists())
print(a.absolute())  # 绝对路径
print(list(a.iterdir()))

a = Path("./data1")
print(a.exists())
a.mkdir(exist_ok=True)
print(a.exists())
print(a.is_dir())

a = Path(".")
a1 = a / "README.md"
print(a1)
a2 = a1.absolute()
print(a2)

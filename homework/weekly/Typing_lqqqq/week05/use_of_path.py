from pathlib import Path

# from pprint import pprint    进行排序

p = Path(".")
print(p)
print(p.exists())
print(p.absolute())
print(list(p.iterdir()))  # 迭代器


p = Path("./data1")
print(p.exists())
p.mkdir(exist_ok=True)
print(p.exists())
print(p.is_dir())


p = Path(".")
p2 = p / "README.md"
print(p2)
p3 = p2.absolute()
print(p3)
breakpoint()

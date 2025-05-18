from Pathlib import Path

p = Path(",")
print(p)
print(p.exists())
print(p.absolute())
print(list(p.iterdir()))


p = Path("./data1")
print(p.exsists())
print(p.is_dir())

p = Path(",")
p2 = p / "README md"
print(p2)
p3 = p2.absolute()
print(p3)
breakpoint()

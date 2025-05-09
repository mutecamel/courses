from pathlib import Path

p = Path(".")
print(p)
print(p.exists())
print(p.absolute())
print(p.iterdir())

p = Path("./data1")
print(p.exists())
p.mkdir
print(p.exists())
print(p.is_dir())

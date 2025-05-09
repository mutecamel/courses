from pathlib import Path

p = Path(".")
print(p)
print(p.exists())
print(p.absolute())
print(list(p.iterdir()))

p = Path("./data1")
print(p.exists())
p.mkdir(exist_ok=True)
print(p.exists())
print(p.is_dir())

p = Path(".")
pp = p / "README,md"
print(pp)
ppp = pp.absolute()
print(ppp)
breakpoint()

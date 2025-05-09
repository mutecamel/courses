from pathlib import Path
from pprint import pprint

p = Path(".")
print(p)
print(p.exists())
print(p.absolute())
pprint(list(p.iterdir()))

p = Path("./detal")
print(p.exists())
p.mkdir(exist_ok=True)
print(p.exists())
print(p.is_dir())

p = Path(".")
p2 = p / "README,md"
print(p2)
p3 = p2.absolute()
print(p3)

from pathlib import Path  # noqa: F401
from pprint import pprint

p = Path(".")
print(p)
print(p.exists())
print(p.absolute())
pprint(list(p.iterdir()))

p = Path("./data")
print(p.exists())
p.mkdir(exist_ok=True)
print(p.exists())
print(p.is_dir())


p = Path(".")
p1 = p / "README.md"
print(p1)
p2 = p1.absolute()
print(p2)

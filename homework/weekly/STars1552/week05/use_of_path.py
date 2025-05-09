from pathlib import Path
from pprint import pprint

p = Path(".")
print(p)
print(p.exists())
print(p.absolute())
pprint(list(p.iterdir()))

p = Path("./data1")
print(p.exists())
p.mkdir()
print(p.exists())
print(p.is_dir())

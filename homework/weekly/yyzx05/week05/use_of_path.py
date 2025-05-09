from pathlib import Path
from pprint import pprint

p = Path(".")
print(p)
print(p.exists())
print(p.absolute())
print(list(p.iterdir()))

p = Path('./datal')
print(.exists())
p.mkdir()
print(p.exists())
print(p.is_dir())

p = Path('.')
p2 = p/"README.md"
print(p2)
p3 = p2.absolute()
print(p3)

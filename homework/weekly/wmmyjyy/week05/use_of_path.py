from pathlib import Path

p = Path(".")
print(p)
print(p.exists())
print(p.absolute())
print(list(p.iterdir()))

from pathlib import Path
from pprint import pprint

p = Path(".")
print(p)
print(p.exists())  #  true
print(p.absolute())  #   C:\Users\mate\repo\week05  绝对路径
pprint(list(p.iterdir()))


p = Path("./data1")
print(p.exists())  # false
p.mkdir(exist_ok=True)
print(p.exists())  # true
print(p.is_dir())  # true

p = Path(".")
p2 = p / "README.md"
print(p2)  #  README.md
p3 = p2.absolute()
print(p3)  #    C:\Users\mate\repo\week05\README.md
print(type(p3))  #   <class 'pathlib.WindowsPath'>
breakpoint()

from pathlib import Path
from pprint import pprint

p = Path(".")  ##.表示当前目录
print(p)
print(p.exists())  ##判断该路径是否存在
print(p.absolute())  ##获得绝对路径
pprint(
    list(p.iterdir())
)  ##列举该路径下的文件,iterdir只是迭代出来的东西，还需要通过列表来呈现

##可以通过mkdir在该路径下新建文件夹
p = Path("./new folder")
print(p.exists())
p.mkdir(exist_ok=True)  ##已经存在该文件不会报错
print(p.exists())
print(p.is_dir())

p = Path(".")
p2 = p / "README.md"  ##p路径下的文件
print(p2)
p3 = p2.absolute()
print(p3)

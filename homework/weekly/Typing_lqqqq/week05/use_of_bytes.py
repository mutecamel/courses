s = b"hello"
print(s[0])  # 输出104 其实是h的序号（二进制）

from pathlib import Path  # 在代码开头添加导入语句，明确引入 Path 类

p = Path("D:\\86157\\anaconda3\\envs\\week05//python.exe")
sorted = p.read_bytes()
print(len(s))  # 查看长度
p = Path("environment.yml")
b = p.read_bytes()
print(s[0])

s = b.decode()
assert isinstance(s, str)
b2 = s.encode()
assert isinstance(b2, bytes)
assert b2 == b
# 字符串可以编码编程字节串，字节串可以解码编程字符串
s = "你好"
b1 = s.encode("utf-8")
print(b1)
b2 = s.encode("gbk")  # 两者编出的结果不一样
print(b2)
s = "abc你好😄"
print(s)
b = s.encode()

breakpoint()

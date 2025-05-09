from pathlib import Path

s = b"hello"
print(s)
print(s[0])

p = Path("D:\\App\\anaconda\\program\\envs\\week05\\python.exe")
s = p.read_bytes()
print(len(s))

p = Path("environment.yml")
b = p.read_bytes()
print(b[0])

s = b.decode()
assert isinstance(s, str)
b2 = s.encode()
assert isinstance(b2, bytes)
assert b2 == b

s = "贝贝"
b1 = s.encode("utf-8")
print(b1)
b2 = s.encode("gbk")
print(b2)
b3 = s.encode("GB2312")
print(b3)

s = "💧"
print(s)
b = s.encode()
breakpoint()

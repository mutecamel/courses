from pathlib import Path

s = b"hello"
print(s)
print(s[0])

p = Path("C:\\Users\\刘佳骏\\repo\\week05\\use_of_bytes.py")
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

s = "你好"
b = s.encode()
print(b)
b2 = s.encode("gbk")
print(b2)

s = "wdawdaasd🥰"
print(s)
b = s.encode()

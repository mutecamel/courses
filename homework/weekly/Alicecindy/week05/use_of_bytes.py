from pathlib import Path

s = b"hello"
print(s)
print(s[0])

p = Path("environment.yml")
b = p.read_bytes()
print(b[0])

s = b.decode()
assert isinstance(s,str)
b2 = s.encode()
assert isinstance(b2,bytes)
assert b2 == b

s = "你好"
b1 = s.encode()
print(b1)
b2 = s.encode("gbk")
print(b2)
breakpoint

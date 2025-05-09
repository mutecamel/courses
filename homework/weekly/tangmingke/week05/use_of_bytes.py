from pathlib import Path

s =b'hello'
print(s)
print(s[0])

p = Path("/d/ana2/envs/week05/python")
s = p.read_bytes()
print(len(s))

p = Path("enviroment.yml")
s = p.read_bytes()
print(s[0])

s = b.decode()
assert isinstance(s, str)
b2 = s.encode()
assert isinstance(b2, bytes)
assert b2 == b

s = "你好"
b1 = s.encode("utf-8")
print(b1)
b2 = s.encode("gbk")
print(b2)

s = "abc你好😀"
print(s)
b = s.encode()
breakpoint()

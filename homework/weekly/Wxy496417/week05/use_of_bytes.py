from pathlib import Path

s = b"hello"
print(s)
print(s[0])

p = Path("D:\\Anaconda\\envs\\week05\\python.exe")
s = p.read_bytes()
print(len(s))

p = Path("use_of_str.py")
b = p.read_bytes()
print(s[0])

s = b.decode()
assert isinstance(s, str)
b2 = s.encode()
assert isinstance(b2, bytes)
assert b2 == b

s = "春天"
b1 = s.encode("utf-8")
print(b1)
b2 = s.encode("gbk")
print(b2)

s = "wa哇😀"
print(s)
b = s.encode()
print(b)
breakpoint()

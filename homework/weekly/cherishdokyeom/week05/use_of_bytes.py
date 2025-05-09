from pathlib import Path

a = b"dokyeom"
print(a)
print(a[0])

p = Path("F:\\biancheng\\Anaconda\\envs\\week05\\python.exe")
s = p.read_bytes()
print(len(s))

p = Path("environment.yml")
s = p.read_bytes()
print(s[0])

m = s.decode()
assert isinstance(m, str)
n = m.encode()
assert isinstance(n, bytes)

L = "李硕珉"
l1 = L.encode("utf-8")
l2 = L.encode("gbk")
print(l1)
print(l2)

s = "李硕珉🐶"
print(s)
b = s.encode()
breakpoint()

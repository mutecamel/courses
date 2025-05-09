from pathlib import Path

s = b"sport"
print(s)
print(s[0])
p = Path("/opt/anaconda3/envs/week05/bin/python")
a = p.read_bytes()
print(len(a))

p = Path("environment.yml")
b = p.read_bytes()
print(b[0])

s = b.decode()
assert isinstance(s, str)
b2 = s.encode()
assert isinstance(b2, bytes)
assert b2 == b

s = "哈嘿啊嘿"
b1 = s.encode("utf-8")
print(b1)
b2 = s.encode("gbk")
print(b2)

sss = "abc我是一个📅"
print(sss)
bbb = sss.encode()


breakpoint()

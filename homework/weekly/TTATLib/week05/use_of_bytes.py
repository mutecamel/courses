from pathlib import Path

s = b'hello'
print(s) 

p = Path("d:\\anaconda\\envs\\week05\\python.exe")
s = p.read_bytes()





S = "你好"
b1 = s.encode()
print(b1)
b2 = s.encode("gbk")
print(b2)
breakpoint()
from pathlib import Path

s = b"hamburger"
print(s)
print(s[0])  #  字面值104

p = Path("D:\\ananconda\\envs\\week05\\python.exe")
s = p.read_bytes()
print(len(s))  #  打印变量s的长度，即文件内容的字节数 93184

p = Path("environment.yml")
b = p.read_bytes()
print(b[0])  # 110 在ASCII编码中，110对应的字符是'n'

s = b.decode()  #  字节串 解码 得到字符串
assert isinstance(s, str)
b2 = s.encode()  # 字符串 编码 得到字节串
assert isinstance(b2, bytes)
assert b2 == b

s = "假期"  #  字符串
b1 = s.encode("utf-8")  # b'\xe5\x81\x87\xe6\x9c\x9f' 字节  16进制  不写默认utf-8
print(b1)  #  b'\xe5\x81\x87\xe6\x9c\x9f'
b2 = s.encode("gbk")  #  gbk编码
print(b2)  # b'\xbc\xd9\xc6\xda'

s = "nihao你好7227🤩"
print(s)
b = s.encode()  #  b'nihao\xe4\xbd\xa0\xe5\xa5\xbd7227\xf0\x9f\xa4\xa9'
print(b)
assert b[5:] == b"\xe4\xbd\xa0\xe5\xa5\xbd7227\xf0\x9f\xa4\xa9"  # 索引
assert b[11:] == b"7227\xf0\x9f\xa4\xa9"
assert isinstance(b, bytes)


breakpoint()

from pathlib import Path

s = b"seventeen"
print(s)
print(s[0])  ##保存的是字节，参考ASCII Table

p = Path("D:\\anaconda\\envs\\week05\\python.exe")
s = p.read_bytes()
print(len(s))  ##显示该路径下的文件大小

p = Path("environment.yml")
b = p.read_bytes()
print(b[0])
s = b.decode()  ##将字节解码成字符串
assert isinstance(s, str)
b2 = s.encode()  ##再将字符串编码成字节
assert isinstance(b2, bytes)
assert b2 == b

s = "格物致知"
b1 = s.encode("utf-8")  ##16进制编码（\x表示16进制，bin([3])显示对应的2进制
print(b1)
b2 = s.encode("gbk")  ##不同的编解码器，默认编码使用utf-8
print(b2)

s = "😅😅😃😃"  ##emoji也可以是字符串所以也可以被编解码
print(s)
b = s.encode()

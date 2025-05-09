from pathlib import Path

s = b"hello"
print(s)
print(s[0])  # 104指h对应ASCLL TABLE的序号104(关于二进制)

p = Path("/opt/anaconda3/envs/week05/bin/python")
s = p.read_bytes()
print(len(s))

p = Path("environment.yml")
b = p.read_bytes()
print(b[0])

s = b.decode()  # 解码转化为字符串
assert isinstance(s, str)
b2 = s.encode()  # 编码转化为字节
assert isinstance(b2, bytes)
assert b2 == b

s = "你好"
b1 = s.encode("utf-8")  # b'\xe4\xbd\xa0\xe5\xa5\xbd'
print(b1)
b2 = s.encode("gbk")
print(b2)

s = "abc你好👋"
print(s)
b = s.encode()

# 字节串的拼接
b1 = b"hello"
b2 = b" world"
b_combined = b1 + b2
print(b_combined)
# 遍历字节串
b = b"test"
for byte in b:
    print(byte)
# 字节串切片
b = b"example"
b_slice = b[1:4]
print(b_slice)
# 检查字节串是否以特定字节串开头结尾
b = b"python is great"
print(b.startswith(b"python"))
print(b.endswith(b"great"))
# 查找字节在字节串中的位置
b = b"byte example"
index = b.find(b"ex")
print(index)

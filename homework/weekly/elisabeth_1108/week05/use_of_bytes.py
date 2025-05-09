from pathlib import Path

s = b'smile'
print(s)

p = Path("C:\\Users\\smile\\anaconda3\\python.exe")
s = p.read_bytes()
print(len(s))

p = Path("environment.yml")
b = p.read_bytes()
print(s[0])

s = b.decode()
assert isinstance(s, str)
b2 = s.encode()
assert isinstance(b2, bytes)
assert b2 == b

s = "你坏"
b = s.encode()

a = 10
b = 3
print(a + b)  # 输出: 13
print(a - b)  # 输出: 7
print(a * b)  # 输出: 30
print(a // b)  # 输出: 3，整数除法
print(a % b)  # 输出: 1，取模运算

# 可以表示非常大的整数
large_number = 123456789012345678901234567890
print(large_number)

breakpoint()

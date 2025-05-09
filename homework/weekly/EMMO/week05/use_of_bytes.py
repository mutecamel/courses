from pathlib import Path

a = b"fzk"
print(a)
print(a[0])

# 使用原始字符串指定文件路径
p = Path(r"D:\anaconda3\python.exe")

try:
    # 调用 read_bytes 方法读取文件内容
    s = p.read_bytes()
    print(s[0])
    print(len(s))
except FileNotFoundError:
    print(f"文件 {p} 未找到。")
except Exception as e:
    print(f"读取文件时出现错误: {e}")

p = Path("environment.yml")
try:
    # 正确调用 read_bytes 方法
    s = p.read_bytes()
    print(s[0])
    print(len(s))
except FileNotFoundError:
    print(f"文件 {p} 未找到。")
except Exception as e:
    print(f"读取文件时出现错误: {e}")

c = s.decode()
assert isinstance(c, str)
b2 = c.encode()
assert isinstance(b2, bytes)
assert b2 == s

y = "大家好,ljj"
o = y.encode("utf-8")
print(y)
print(o)
o1 = y.encode("gbk")
print(o1)


w = "你是小🐖"
q = w.encode()
print(w)
print(q)

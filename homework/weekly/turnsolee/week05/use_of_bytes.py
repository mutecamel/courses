from pathlib import Path

s = "你好，世界"
print(s)

p = Path("D:\\ananconda3\\envs\\week05")
s = p.read_bytes()
print(len(s))

p = Path("environment.yml")
b = p.read_bytes()
print(b[0])

# 字符串编码为字节
s_encoded = s.encode('utf-8')
print(s_encoded)

# 字节解码为字符串
s_decoded = s_encoded.decode('utf-8')
print(s_decoded)

# 断言检查类型
assert isinstance(s, str)
assert isinstance(s_encoded, bytes)

# 包含特殊字符的字符串操作
s_with_special = "abc你好😀"
print(s_with_special)
b_special = s_with_special.encode('utf-8')
print(b_special)

breakpoint()

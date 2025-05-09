# 字节串 (bytes)
bytes_example = b"Hello, Bytes!"

# 使用内置函数检视对象
print(f"ID: {id(bytes_example)}")
print(f"Type: {type(bytes_example)}")
print(f"Is instance of bytes: {isinstance(bytes_example, bytes)}")
print(f"Attributes and methods: {dir(bytes_example)}")
print(f"Bytes representation: {str(bytes_example)}")

# 数学运算符支持
try:
    result = bytes_example + b" Python"
    print(f"Concatenation: {result}")
except TypeError as e:
    print(e)

# 判断相等
assert bytes_example == b"Hello, Bytes!", "Bytes are not equal"

# 比较运算符支持
another_bytes = b"Hello, Universe!"
if another_bytes > bytes_example:
    print("another_bytes is greater than bytes_example")

# 布尔值判断
empty_bytes = b""
non_empty_bytes = b"Non-empty"
print(f"Empty bytes evaluates to: {bool(empty_bytes)}")
print(f"Non-empty bytes evaluates to: {bool(non_empty_bytes)}")

# 可迭代性
for byte in bytes_example:
    print(byte, end=" ")
print()

# 长度
print(f"Length of bytes_example: {len(bytes_example)}")

# 索引操作
print(f"First byte: {bytes_example[0]}")
print(f"Last byte: {bytes_example[-1]}")

# 常用方法
print(f"Hexadecimal: {bytes_example.hex()}")
print(f"From hexadecimal: {bytes.fromhex('48656c6c6f2c20427974657321')}")

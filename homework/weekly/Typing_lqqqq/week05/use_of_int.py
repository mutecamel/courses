# 加减
i = 42
x = 5
y = 7
z = x + y
# 除法
x = 3
y = 19
assert y // x == 6  # 有6个3
assert y % x == 1  # 余数为1 没报错正确

assert 5
# assert 0#会报错，0会当成false
try:
    assert 0
except AssertionError as e:
    print(e)  # 会有空行

x = 8837  # 字节过大
breakpoint()
# 整数不可循环迭代

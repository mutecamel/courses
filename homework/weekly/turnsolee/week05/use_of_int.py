a = 42
b = 5
c = 7
# 加法运算
result_sum = a + b
print(f"{a} + {b} 的结果是: {result_sum}")
# 除法运算并断言结果
d = 21
e = 7
assert d / e == 3, "除法运算结果不符合预期"
# 取余运算并断言结果
f = 17
g = 5
assert f % g == 2, "取余运算结果不符合预期"

# 使用try - except捕获断言错误
try:
    # 故意设置一个错误的断言
    assert 0
except AssertionError as e:
    print(f"捕获到断言错误: {type(e)}")

# 定义一个整数并进入调试模式
num = 666

breakpoint()

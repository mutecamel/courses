import random

m = 9.10
print(type(m))

n = float("9.10")
print(type(n))

assert m == n

x = 10 / 9
print(x, type(x))

y = random.random()
print(y)

# assert 0.0
assert not 0.0

nan = float("nan")  # nan:特殊的浮点数，可看作缺失值
print(nan + 10)  # 结果仍为nan
print(nan > 10)  # 结果为False
print(nan < 10)  # 结果为False
print(nan == 10)  # 结果为False

pinf = float("inf")  # 正无穷
print(9e-10)
print(pinf > 9e10)  # 结果为True
print(pinf > pinf)  # 结果为False
print(pinf == pinf)  # 结果为True

ninf = float("-inf")  # 负无穷
print(ninf)

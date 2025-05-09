##整数对数学运算符都支持
x = 5
y = 2
assert x / y == 2.5
assert x // y == 2  ##整除
assert x % y == 1  ##余除显示余数


##0显示为False,整数不可迭代，也不可提取
try:
    assert 0
except AssertionError as e:
    print(type(e))

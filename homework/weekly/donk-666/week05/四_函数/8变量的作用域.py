"""
def test_a()
    num=100
    print(num)

test_a()
print(num)
#局部变量只能在局部使用 全局变量可以在函数内部和外部使用
"""
#global关键字，在函数内声明变量是全局变量
num=200
def test_a():
    print(f"test_a:{num}")
def test_b():
    global num
    num=500
    print(f"test_b:{num}")
test_a()
test_b()
print(num)

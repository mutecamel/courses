from mylib import *

# 调用 func1
func1()

# 调用 func2
result2 = func2()
print(f"func2 返回值: {result2}")

# 调用 func3
func3(5)
func3(a=10)
try:
    func3()
except TypeError:
    print("func3 不传参报错")

# 调用 func4
func4(5)
func4(a=10)
func4()

# 调用 func5
func5(1, 2)
func5(1, 2, 3)
func5(1, b=2, c=3)

# 调用 func6
func6(1, 2)
try:
    func6(a=1, b=2)
except TypeError:
    print("func6 不能用命名传 a")

# 调用 func7
func7(a=5)
try:
    func7(5)
except TypeError:
    print("func7 不能位置传参")

# 调用 func8
func8(1, 2, 3)

# 调用 func9
func9(a=1, b=2)

# 调用 func10（解包列表）
lst = [1, 2]
func10(*lst, c=4)

# 调用 func11（解包字典）
dct = {'b':4, 'c':5}
func11(1, **dct)

# 调用 func12
print(f"func12 结果: {func12(3, 5)}")
print(func12.__doc__)
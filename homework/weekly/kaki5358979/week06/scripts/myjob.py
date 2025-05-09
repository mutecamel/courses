from mypkg import mylib  # noqa: F401

y = mylib.func1()
print(y)  # None

try:
    y = mylib.func1(0)
except TypeError as e:  # 不报错，返回错误信息
    print(e)


y = mylib.func2()
print(y)  # 2


y = mylib.func3(60)  # 传入位置实参(positional argument)调用
print(y)

y = mylib.func3(x=60)  # 传入命名实参(named argument)调用
print(y)

try:
    y = mylib.func3()  # 不传实参报错
except TypeError as e:
    print(e)


y = mylib.func4(60)  # 传入位置实参(positional argument)调用
print(y)

y = mylib.func4(x=60)  # 传入命名实参(named argument)调用
print(y)

y = mylib.func4()  # 不传实参取默认值
print(y)


y = mylib.func5(10, 6)
print(y)

y = mylib.func5(10, 6, "substract")
print(y)


try:
    y = mylib.func6(a=10, b=6)
except TypeError as e:
    print(e)

try:
    y = mylib.func7(10, 6, "substract")
except TypeError as e:
    print(e)

print(mylib.func8(4, 8, 8))

mylib.func9(name="Jac", city="LA")

args = (10, 20)  # 元组
mylib.func10(*args, name="Bob")

kwargs = {"name": "Bob", "age": 30}
mylib.func11(20, **kwargs)

print(mylib.func12("Mia", 23))

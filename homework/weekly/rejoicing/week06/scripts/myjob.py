import mylib  # noqa: F401

y = mylib.func1()
print(y)

try:
    y = mylib.func1(1)  # 修改传入的参数为 1
except TypeError as e:
    print(e)

y = mylib.func2()
print(y)

y = mylib.func3(60)  # 修改传入的参数为 60
print(y)
y = mylib.func3(x=80)  # 修改传入的参数为 80
print(y)
try:
    y = mylib.func3()
except TypeError as e:
    print(e)

y = mylib.func4(25)  # 修改传入的参数为 25
print(y)
y = mylib.func4(x=90)  # 修改传入的参数为 90
print(y)
y = mylib.func4()
print(y)


print(mylib.area1)
print(mylib.area2)

try:
    print(mylib.func6(a=20, b=180))  # 修改传入的参数 a 为 20，b 为 180
except TypeError as e:
    print(e)


print(mylib.func7(20, 180))  # 修改传入的参数为 20 和 180

print(mylib.func8(20, 180, 83000))  # 修改传入的第三个参数为 83000
print(mylib.func8(20, 180, 83000, 74000, 2900))  # 修改传入的部分参数
print(mylib.func8(20, 180))  # 修改传入的参数为 20 和 180

mylib.func9(name="Bob", age=28, city="Los Angeles")  # 修改传入的参数

tuple_args = (3, 4)  # 修改元组参数
mylib.func10(*tuple_args)
list_args = [6, 8]  # 修改列表参数
mylib.func10(*list_args, named_arg=25)  # 修改命名参数的值

mylib.func12(73000, 33000, 380)  # 修改传入的参数

import scripts.src.mypkg.mypkg2.mylib as mylib  # noqa:F401

y = mylib.func1()
print(y)

try:
    y = mylib.func1(0)
except TypeError as e:
    print(e)

y = mylib.func2()
print(y)

y = mylib.func3(45)
print(y)

y = mylib.func3(x=45)
print(y)

try:
    y = mylib.func3()
except TypeError as e:
    print(e)
try:
    y = mylib.func3(y=47)
except TypeError as e:
    print(e)

y = mylib.func4(48)
print(y)

y = mylib.func4(x=49)
print(y)

y = mylib.func4()
print(y)

print(mylib.calculate(1, b=2, c=3))
print(mylib.calculate(1, 3, c=3))


print(mylib.func6(10, 1, 3))


print(mylib.func7(10, b=1, c=3))

print(mylib.func8(4, 8, 18))
print(mylib.func8(4, 8, 18, 5))

mylib.func9(name="张三", age=25, city="北京")

my_list = [10, 20]
mylib.func10(*my_list, option="new_value")
my_tuple = (30, 40)
mylib.func10(*my_tuple, option="another_value")

mylib.func12(7, 8, 9)

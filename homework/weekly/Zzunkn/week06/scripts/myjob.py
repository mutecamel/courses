from mypkg import mylib

y = mylib.func1()
print(y)

try:
    y = mylib.func2(0)
except TypeError as e:
    print(e)

y = mylib.func2()
print(y)

y = mylib.func3(55)
print(y)

try:
    y = mylib.func3(x=45)
except TypeError as e:
    print(e)

y = mylib.func4(50)
print(y)

print(mylib.func5(4))

print(mylib.func8(4, 8))

mylib.func9(name="Alice", age=25, city="New York")

my_tuple = (10, 20)
mylib.func10(*my_tuple, named_arg="custom")

mylib.func12(7, 7, 9)

import mylib

y = mylib.func1()
print(y)

try:
    y = mylib.func2(0)
except TypeError as e:
    print(e)

y = mylib.func2()
print(y)

y = mylib.func3(100)
print(y)
y = mylib.func3(x=100)
print(y)
try:
    y = mylib.func3()
except TypeError as e:
    print(e)

y = mylib.func4()
print(y)

print(mylib.func6(70, b=80, operation="subtract"))

print(mylib.func8(4, 8, 9, 4))
mylib.func9(name="刘家俊", age="23", city="北京")

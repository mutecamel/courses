import src.mypkg.mylib as mylib  # noqa: F401

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


y = mylib.func3(x=47)
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

try:
    print(mylib.func6(a=10, b=5))
except TypeError as e:
    print(e)


try:
    print(mylib.func7(10, 5, "subsract"))
except TypeError as e:
    print(e)

print(mylib.func8(4, 8))
print(mylib.func9(name="Alice", age=25, city="New York"))

tuple_arges = (10, 20)
mylib.func10(*tuple_arges)

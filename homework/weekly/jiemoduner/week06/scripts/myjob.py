import mylib  # noqa: F401

y = mylib.func1(0)
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
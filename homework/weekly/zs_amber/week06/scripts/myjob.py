from mypacket import mylib  # noqa:F401

y = mylib.func1()
print(y)

y = mylib.func2()
print(y)

y = mylib.func3(45)
print(y)
y = mylib.func3(x=45)
print(y)

y = mylib.func4(48)
print(y)
y = mylib.func4(x=49)
print(y)
y = mylib.func4()
print(y)

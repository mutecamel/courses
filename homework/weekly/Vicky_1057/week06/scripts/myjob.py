from mypkg import mylib

y = mylib.func1
print(y)

y = mylib.func3(45)
print(y)  # 位置实参

y = mylib.func3(x=47)
print(y)  # 命名实参

y = mylib.func4(47)
print(y)  # 位置实参

y = mylib.func4(x=49)
print(y)  # 命名实参

y = mylib.func4()
print(y)  # 不传实参

print(mylib.caculate(5, 10, "add"))
print(mylib.caculate(operation="add", b=5, a=10))
print(mylib.caculate(b=5, a=10))
print(mylib.caculate(5, 10, operation="subtract"))

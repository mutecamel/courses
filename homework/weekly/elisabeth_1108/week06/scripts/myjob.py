from mypkg import mylib  # noqa: F401

y = mylib.func1()
print(y)

try:
    y = mylib.func1(0)
except TypeError as e:
    print(e)


y = mylib.func2()
print(y)

y = mylib.func3(x=47)
print(y)

y = mylib.func4(48)
print(y)

y = mylib.func4(x=49)
print(y)


y = mylib.func4()
print(y)

print(mylib.func5(10, 5, "add"))
print(mylib.func5(operation="add", b=5, a=10))
print(mylib.func5(5, 8, operation="subtract"))

# print(mylib.func6(a=10, b=5))

# try:
#   print(mylib.func6(a=10, b=5))
# except TypeError as e:
#    print(e)

print(mylib.func7(10, 5, operation="subtract"))

print(mylib.func8(4, 8, 18))

print(mylib.func9(name="Alice", age=25, city="New York"))

args_tuple = (10, 20)
mylib.func10(*args_tuple, named_arg="custom")

args_list = [30, 40]
mylib.func10(*args_list, named_arg="new_custom")

params = {"arg1": 1, "arg2": 2, "arg3": 3}
print(mylib.func11(**params))

print(mylib.func12(2, 3))

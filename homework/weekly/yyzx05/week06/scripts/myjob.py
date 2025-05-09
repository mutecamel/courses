from mypkg import mylib  # 12345

y = mylib.func1()
print(y)

try:
    y = mylib.func1(0)
except TypeError as e:
    print(e)

y = mylib.func2()
print(y)

y = mylib.func2_2()
print(y)

y = mylib.func3(45)
print(y)

y = mylib.func3(x=65)

try:
    y = mylib.func3(0)
except TypeError as e:
    print(e)

y = mylib.func4(34)
print(y)

y = mylib.func4(x=34)
print(y)

y = mylib.func4()
print(y)

y = mylib.func5(10, quantity=2, discount=0.1)
print(y)

try:
    y = mylib.func6(a=10, b=8)
except TypeError as e:
    print(e)

y = mylib.func7(8, 10)
print(y)

y = mylib.func8(1, 2, 3, 4, 5)
print(y)

y = mylib.func9(name="John", age=25, city="New York")
print(y)

iterable_obj = (3, 5)
y = mylib.func10(*iterable_obj, named_arg=2)
print(y)

my_dict = {"param1": 10, "param2": 20, "param3": 30}

y = mylib.func11(**my_dict)
print(y)

iterable_obj = (2.2, 9)
y = mylib.func12(*iterable_obj, named_arg=2)
print(y)

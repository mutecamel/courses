import mylib  # noqa: F401

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
    mylib.func3(y=47)
except TypeError as e:
    print(e)

y = mylib.func4(48)
print(y)

y = mylib.func4(x=49)
print(y)

y = mylib.func4()
print(y)

print(mylib.calculate_total(10, 5, 0.1, 0))
print(mylib.calculate_total(price=20, quantity=3, tax_rate=0.15, discount=0.1))
print(mylib.calculate_total(10, 5, tax_rate=0.2, discount=0.05))

try:
    print(mylib.func6(price=20, quantity=3))
except TypeError as e:
    print(e)

try:
    print(mylib.func7(10, 5, 0.1, 0))
except TypeError as e:
    print(e)

print(mylib.func8(4, 8))
print(mylib.func8(4, 8, 12))

mylib.func9(name="Alice", age=25, city="New York")

tuple_poses = (10, 20)
mylib.func10(*tuple_poses)

list_poses = [30, 40]
mylib.func10(*list_poses)

list_poses = [50, 60, "new value"]
mylib.func10(*list_poses)

mapping_obj = {"named_arg1": 100, "named_arg2": 200}
mylib.func11(5, **mapping_obj)

mylib.func12(7, 8, 9)
breakpoint()

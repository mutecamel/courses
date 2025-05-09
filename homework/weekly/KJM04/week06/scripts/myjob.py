from mypkg import mylib

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

print(mylib.process_order(product_name="智能手机", unit_price=5000))
print(mylib.process_order(product_name="手机", unit_price=4999))

try:
    print(mylib.func6("手机", "4998"))
except TypeError as e:
    print(e)

print(mylib.func7("手机", "4997"))

print(mylib.func8(4, 8))

mylib.func9("Alice", 25, city="New York", occupation="Doctor")

iterable_obj = (20, 30)
mylib.func10(*iterable_obj, named_arg=40)

mapping_obj = {"param1": 10, "param2": 20, "param3": 30}
mylib.func11(**mapping_obj)

mylib.func12(7, 8, 9)

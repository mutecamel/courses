from mypkg import mylib  # noqa: F401

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

y = mylib.func4()
print(y)

mylib.func5(10, 5, "平方米")
mylib.func5(unit="平方米", width=5, length=10)

try:
    print(mylib.func6(a=10, b=5))
except TypeError as e:
    print(e)

try:
    print(mylib.func7(10, 5, "平方米"))
except TypeError as e:
    print(e)

mylib.func7(10, 5, unit="平方米")

print(mylib.func8(4, 8, 18))

mylib.func9(name="John", age=25, city="New York")

tuple_data = (10, 20)
mylib.func10(*tuple_data)
list_data = [5, 15]
mylib.func10(*list_data)
list_data = [50, 60, "new value"]
mylib.func10(*list_data)

person = {"name": "Bob", "age": 30}
mylib.func11(**person)

mylib.func12(7, 8, 9)

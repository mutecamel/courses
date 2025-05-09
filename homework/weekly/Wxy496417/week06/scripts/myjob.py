from mypkg import mylib  # noqa: F401

y = mylib.func1()
print(y)

try:
    y = mylib.func1(0)
except TypeError as e:
    print(e)

y = mylib.func2()
print(y)

y = mylib.func3(70)
print(y)

y = mylib.func3(x=55)
print(y)

try:
    y = mylib.func3()
except TypeError as e:
    print(e)

try:
    y = mylib.func3(y=55)
except TypeError as e:
    print(e)

y = mylib.func4(50)
print(y)

y = mylib.func4(x=49)
print(y)

y = mylib.func4()
print(y)

score1 = mylib.calculate_score(80, 15, False)
print(score1)

score2 = mylib.calculate_score(bonus=15, base_score=80, special_reward=False)
print(score1)

score3 = mylib.calculate_score(bonus=15, base_score=80)
print(score1)

score4 = mylib.calculate_score(90, 16, special_reward=True)
print(score4)

try:
    print(mylib.func6(base_score=70, bonus=20))
except TypeError as e:
    print(e)

try:
    print(mylib.func7(70, 20, "False"))
except TypeError as e:
    print(e)

print(mylib.func7(70, 20, special_reward=True))

print(mylib.func8(3, 4, 5, 20))
print(mylib.func8())

mylib.func9(name="Alice", age=25, city="New York")
mylib.func9()

args_tuple = (20, 30)
result = mylib.func10(*args_tuple)
print(result)

args_list = [30, 40]
print(mylib.func10(*args_list))

args_list = [30, 40, 20]
result = mylib.func10(*args_list)
print(result)

params_dict = {"param1": 10, "param2": 20, "param3": 30}
result = mylib.func11(**params_dict)
print(result)

mylib.func12(10, 20)

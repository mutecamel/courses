from mypkg import mylib

y = mylib.func1()
print(y)

y = mylib.func2()
print(y)

y = mylib.func3(85)
print(y)

y = mylib.func3(x=95)
print(y)

y = mylib.func4(48)
print(y)

y = mylib.func4(x=49)
print(y)

print(mylib.calculate_area(10))

print(mylib.func6(10))

print(mylib.func8(4, 8, 18))

print(mylib.func9(name="Alice", age=25, city="New York"))

data_tuple = (20, 30)
mylib.func10(*data_tuple)
data_list = [5, 15]
mylib.func10(*data_list)

# 定义 func11 函数，接受三个命名形参
def func11(param1=0, param2=1, param3=2):
    print(f"param1 的值是: {param1}")
    print(f"param2 的值是: {param2}")
    print(f"param3 的值是: {param3}")


# 创建一个字典作为映射对象
data_dict = {
    "param1": 10,
    "param2": 20,
    "param3": 30
}

print("即将调用 func11 函数，传递的参数如下：")
for key, value in data_dict.items():
    print(f"{key}: {value}")
print("开始调用 func11 函数...")
func11(**data_dict)
print("func11 函数调用结束。")




# 调用 mylib 中的 func12 函数
result = mylib.func12(a=5, b=3, multiplier=2.0)
print(f"调用结果: {result}") 

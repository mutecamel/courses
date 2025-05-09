from mypkg import mylib  # noqa:F401

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

y = mylib.func3(x=55)
print(y)
try:
    y = mylib.func3()
except TypeError as e:
    print(e)

y = mylib.func4(48)
print(y)
y = mylib.func4(x=48)
print(y)


print(mylib.calculate_total_price)
print(mylib.calculate_total_price(3, 10))
print(mylib.calculate_total_price(3, 10, discount=0.1))
print(mylib.calculate_total_price(4, price_per_item=15, shipping_fee=8))
print(
    mylib.calculate_total_price(
        quantity=5, price_per_item=12, discount=0.2, shipping_fee=10
    )
)


# 测试 func6
print(mylib.func6(1, 2))
# 以下调用会报错，因为不允许使用命名实参
# print(func6(a=1, b=2))

# 测试 func7
print(mylib.func7(c=3, d=4))
# 以下调用会报错，因为不允许使用位置实参
# print(func7(3, 4))

# 测试 func8
print(mylib.func8(1, 2, 3, 4, 5))

# 测试 func9
print(mylib.func9(10, 5, key1=1, key2=2))

# 测试 func10，使用 * 自动解包可迭代对象
iterable = (3, 4)
print(mylib.func10(*iterable, r=5))

# 测试 func11，使用 ** 自动解包映射对象
mapping = {"s": 1, "t": 2, "u": 3}
print(mylib.func11(**mapping))

mylib.func12(7, 8, 9)

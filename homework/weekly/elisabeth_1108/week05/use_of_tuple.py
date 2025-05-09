t = (1, "a", 3.14)
print(t)

print(t[0])
print(t[1])

try:
    t[0] = 9
except TypeError as e:
    print(e)


d = {}
d["abc"] = 5
d[7] = 100
print(t)

# 创建空元组
empty_tuple = ()
# 创建包含元素的元组
fruits = ('apple', 'banana', 'cherry')

print(fruits[0])  # 输出 'apple'

try:
    fruits[0] = 'grape'
except TypeError:
    print("元组元素不能被修改")

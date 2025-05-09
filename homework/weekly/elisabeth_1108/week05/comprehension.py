# 创建一个包含 1 到 10 的平方的列表
squares = [x**2 for x in range(1, 11)]
print(squares)

# 筛选出列表中的偶数
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)
d = {"a": 1, "gg": 68, "dog": 250, "fish": 878}  # 散列表 无顺序
print(d)  #   {'a': 1, 'gg': 68, 'dog': 250, 'fish': 878}
print(type(d))  #   <class 'dict'>

for a in d:
    print(a)

for a in d:
    print(d[a])

for a in d.values():
    print(a)

l = [a for a in d.items()]
print(l)  #   [('a', 1), ('gg', 68), ('dog', 250), ('fish', 878)]  元组元组元组

for k, v in d.items():
    print(k, v)

try:
    assert {}
except AssertionError as e:
    print(e)

assert not {}

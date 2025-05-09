lst = [1, 2, 3]           # 列表字面值
dct = {'a': 1, 'b': 2}    # 字典字面值
st = {1, 2, 3}            # 集合字面值
s = "hello"               # 字符串字面值
num = 42                  # 整数面值

lst = [x**2 for x in range(5)]

dct = {k: v*2 for k, v in {'a': 1, 'b': 2}.items()}

st = {x%2 for x in [1, 2, 3, 4]}

lst = list()                # 空列表
lst = list((1, 2, 3))       # 从元组转换
dct = dict(a=1, b=2)        # 键值对初始化
st = set([1, 2, 2, 3])      # 去重初始化
s = str(42)                 # 从整数转换为字符串
num = int("42")             # 从字符串转换为整数

lst = [1, 2] + [3, 4]
lst = [0] * 3

s = "hello" + "world"
s = "a" * 3

num = 2 + 3 * 4

lst = [1, 2, 3, 4]
sub_lst = lst[1:3]

dct = {'a': 1, 'b': 2}
new_dct = {k: v for k, v in dct.items() if v > 1}

lst = list(range(5))
dct = dict.fromkeys(['a', 'b'], 0)

s = "  hello  ".strip()
a = {
    "dokyeom": 9,
    "mingyu": 10,
}  # 无所谓顺序（通过键找值），与列表不同 #字典的键必须为不可变（元祖可作为键，但列表不可以）
print(a)
print(type(a))

for i in a:  # 循环的是键：dokyeom、mingyu
    print(i)

for g in a:  # 输出结果是值：9、10
    print(a[g])

for b in a.values():  # 输出结果是值：9、10
    print(b)

c = [d for d in a.items()]  # 输出结果是[('dokyeom', 9), ('mingyu', 10)]
print(c)

for x, y in a.items():  # 输出结果是dokyeom 9（换行）mingyu 10
    print(x, y)
assert not {}  # 字典不空即为True
# breakpoint()

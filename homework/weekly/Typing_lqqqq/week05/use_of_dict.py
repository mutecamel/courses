# 很重要,与列表一样也是容器，列表有顺序，字典没有所谓的顺序，散列表
d = {"a": 1, "bb": 5, "cat": 3}
print(d)
print(type(d))

# 可以用键 用值 用键值对循环，字典比列表复杂
for a in d:
    print(a)

for a in d:
    print(d[a])

for a in d.values:
    print(a)

l = [a for a in d.items()]
print(l)


for k, v in d.items():
    print(k, v)


# 空会当成false
assert {}

breakpoint()

# 哈希值无规律，内部调配的
# l
# p hash('a')
# p hash('b')
# p hash('b')


# p d
# p d["bb"]
# p d["bbb"]
# p d.get['bb']
# p d.get['bbb',0]
# p d.pop('bb')
# p d.setdefault("cat",0)
# p d.setdefault('bb',0)

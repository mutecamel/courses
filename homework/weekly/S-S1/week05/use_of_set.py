a = {477, 293, 626}
print(a)
print(type(a))

try:
    a = {477, [293], 626}
except TypeError as e:
    print(e)

aa = [66, 44, 33, 88, 99, 33, 99]
print(aa)
bb = set(aa)
print(bb)

aa = {66, 44, 33, 88, 99, 33, 99}
print(aa)
print(44 in aa)
print(688 in aa)

cc = {2, 987, 99, 88}
print(cc | aa)
print(cc & aa)
print(cc ^ aa)

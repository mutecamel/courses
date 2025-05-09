s1 = 'hello'
s2 = str(3.14)
s3 = f"{s1} world!"
s4 = s1 + ' python'
s5 = ''.join(['a', 'b', 'c'])

assert id(s1) != id(s2)
assert type(s1) is str
assert isinstance(s3, str)
assert '__len__' in dir(s1)
assert str(s1) == 'hello'

assert 'py' in s4
assert s1 < 'zebra'
assert s1 * 2 == 'hellohello'

assert len(s1) == 5
assert s1[0] == 'h'
try:
    s1[0] = 'H'
except TypeError:
    pass

assert s1.upper() == 'HELLO'
assert 'llo' in s1

assert bool('') is False
assert bool(s1) is True

assert [c for c in s1] == ['h','e','l','l','o']

lst1 = [1, 2, 3]
lst2 = list('abc')
lst3 = [i*2 for i in lst1]
lst4 = lst1 + [4]
lst5 = lst1[1:]

assert id(lst1) != id(lst3)
assert type(lst1) is list
assert isinstance(lst2, list)
assert '__iter__' in dir(lst1)

assert lst1 * 2 == [1,2,3,1,2,3]
assert [1,2] < [1,3]

lst1[0] = 10
assert len(lst1) == 3
assert lst2[-1] == 'c'

lst1.append(4)
assert lst1.pop() == 4

assert bool([]) is False
assert bool(lst1) is True

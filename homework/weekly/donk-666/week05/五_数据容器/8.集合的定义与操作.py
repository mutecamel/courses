#集合{} 集合不允许重复 顺序是没有办法保证的 不支持小标索引访问
#定义集合
my_set={"传智教育","黑马程序员","itheima","传智教育","黑马程序员","itheima","传智教育","黑马程序员","itheima"}
my_set_empty=set() #定义空集合
print(f"my_set的内容是：{my_set},类型是：{type(my_set)}")
print(f"my_set的内容是：{my_set_empty},类型是：{type(my_set_empty)}")

#添加新元素
my_set.add("Python")
my_set.add("传智教育")
print(f"my_set添加元素后的结果是：{my_set}")

#移除元素
my_set.remove("黑马程序员")
print(f"my_set移除黑马程序员后的结果是：{my_set}")

#从集合中随机取出元素
my_set={"传智教育","黑马程序员","itheima"}
element=my_set.pop()
print(f"集合被取出元素是：{element},剩下的元素是:{my_set}")

#清空集合
my_set.clear()
print(f"清空集合是：{my_set}")

#取两个集合的差集
#取出集合1有而集合2没有的
set1={1,2,3}
set2={1,5,6}
set3=set1.difference(set2)
print(set1)
print(set2)
print(set3)

#消除差集：在集合1的内部删除与集合2相同的元素
#结果是集合1变化，集合2不变
set1={1,2,3}
set2={1,5,6}
set1.difference_update(set2)
print(f"消除差集后的结果：{set1}")
print(f"消除差集后的结果：{set2}")

#集合的合并
set1={1,2,3}
set2={1,5,6}
set3=set1.union(set2)
print(f"集合合并的结果{set3},合并后集合：{set1}与{set2}")

#统计集合元素数量
set1={1,2,3,4,5,1,2,3}
num=len(set1)
print(f"集合中的元素数量有{num}个")

#集合的遍历
#集合不支持下标索引，不可以用while循环，可以用for循环
set1={1,2,3,4,5,1,2,3}
for element in set1:
    print(f"集合中的元素有：{element}")
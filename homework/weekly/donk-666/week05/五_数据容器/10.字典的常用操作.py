#字典中新增元素
my_dict={
    "王力宏":99,
    "周杰伦":88,
    "张学友":77
}
#新增张信哲的成绩
my_dict["张信哲"]=66
print(f"字典新增元素后的结果是：{my_dict}")
my_dict["周杰伦"]=33
print(f"字典更新元素后的结果是：{my_dict}")

#删除元素
score=my_dict.pop("周杰伦")
print(f"字典被移除元素的结果：{my_dict}，周杰伦的考试分数是：{score}")

#清空元素
my_dict.clear()
print(f"字典被清空结果是：{my_dict}")

#获取全部的key
my_dict={
    "王力宏":99,
    "周杰伦":88,
    "张学友":77
}
keys=my_dict.keys()
print(f"字典的全部key值是：{keys}")

#字典的遍历
#方式1
for key in keys:
    print(f"字典的key值是：{key}")
    print(f"字典的value值是：{my_dict[key]}")
#方式2
for key in my_dict:
    print(f"字典的key值是：{key}")
    print(f"字典的value值是：{my_dict[key]}")

#统计字典中的元素
num=len(my_dict)
print(f"字典中的元素数量有{num}个")


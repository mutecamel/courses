#字典的定义
my_dict={"王力宏":99,"周杰伦":88,"林俊杰":77}
#定义空字典
my_dict2={}
my_dict3=dict()
print(f"字典1的内容是：{my_dict},类型是：{type(my_dict)}")
print(f"字典2的内容是：{my_dict2},类型是：{type(my_dict2)}")
print(f"字典3的内容是：{my_dict3},类型是：{type(my_dict3)}")
#字典与集合一样，不支持下标索引

#定义重复key的字典
my_dict1={"王力宏":99,"周杰伦":88,"林俊杰":77}
print(f"重复字典的内容是：{my_dict1}")

#从字典中基于key获取value
my_dict1={"王力宏":99,"周杰伦":88,"林俊杰":77}
score=my_dict1["王力宏"]
print(f"王力宏的分数是：{score}")
score=my_dict1["周杰伦"]
print(f"周杰伦的分数是：{score}")

#字典的嵌套
stu_score_dict={
    "王力宏":{
        "语文":77,
        "数学":66,
        "英语":33
    },
    "周杰伦":{
        "语文": 88,
        "数学": 66,
        "英语": 55
    },
    "林俊杰":{
        "语文": 99,
        "数学": 96,
        "英语": 66
    },
}
print(f"学生的考试信息是：{stu_score_dict}")
#从字典中获取信息
score =stu_score_dict["周杰伦"]["语文"]
print(f"周杰伦的语文信息是：{score}")
score =stu_score_dict["林俊杰"]["英语"]
print(f"林俊杰的语文信息是：{score}")
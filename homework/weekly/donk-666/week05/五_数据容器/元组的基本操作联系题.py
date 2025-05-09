t1=("周杰伦",11,["python","music"])
t2=t1.index(11)
print(f"其年龄坐在的下标位置是：{t2}")
t3=t1[0]
print(f"学生的姓名是：{t3}")
type_list=list(t1)
del type_list[2][0]
print(type_list)
type_list[2].append("ding")
print(type_list)
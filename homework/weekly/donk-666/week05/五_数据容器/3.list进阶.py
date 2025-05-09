#寻找某在列表的下标，如果找不到，报错
#语法：列表.index（元素）
mylist=['it','itheima','python']
index=mylist.index('python')
print(index)

#修改某一下标的值
mylist[0]='jiaoyu'
print(mylist)

#列表元素的插入
mylist.insert(1,'best')
print(mylist)

#追加元素 列表.append（元素），将指定元素插入尾部
mylist.append('ji')
print(mylist)

#追加元素，列表.extend，增加新的数据容器
mylist2=[1,2,3]
mylist.extend(mylist2)
print(mylist)

#删除元素
del mylist[2]
print(mylist)
#通过列表.pop可以取出某个元素，通过返回值可以得到
element=mylist.pop(2)

#列表.remove（），移除某个固定的元素
mylist.remove(1)
print(mylist)

#清空列表
mylist.clear()
print(mylist)

mylist=['it','itheima','python','itheima','it']
#统计某元素的数量
num= mylist.count('it')
print(num)

#计算列表元素的数量
num=len(mylist)
print(num)
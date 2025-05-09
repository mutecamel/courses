#基础数据的注解
import json
import random

var_1:int=10
vat_2:str="itheima"
var_3:bool=True
#类对象类型注解
class Student:
    pass
stu:Student=Student()
#基础容器类型注解
my_list:list=[1,2,3]
my_tuple:tuple=(1,2,3)
my_dict:dict={"itheima":666}
#容器类型详细注解
my_list:list[int]=[1,2,3]
my_tuple:tuple[int,str,bool]=(1,'ITHEIMA',True)
my_dict:dict[str,int]={"itheima":666}
#在注释中进行类型注解
var_4=random.randint(1,10)#type:int
var_5=json.loads('{"name":"张三"}')#type:dict[str,str]
def func():
    return 10
var_6=func()#type:int
#类型注解的限制

#函数方法的类型注解
#对形参进行类型注解
def add(x:int,y:int):
    return x+y

#对返回值进行类型注解
def fucn(data:list)->list:
    return data
#类型注解不是强制性的，而是建议性的

#union类型
#使用union类型导包
from typing import Union
mylist:list[Union[int,str]][1,2,'itheima','itcast']
def func1(data:Union[str,int])->Union[str,int]:
    pass


#关键字参数：函数调用时通过“键=值”形式传递参数
#作用：可以让函数更加清晰，容易使用，同时也清除了参数的顺序需求

#关键字参数
def user_info(name,age,gender):
    print(f"姓名是：{name},年龄是：{age},性别是：{gender}")
user_info("小明",20,"男")
user_info(age=10,gender="女",name="小红")#可以不按照参数定义的顺序传参
user_info("田田",gender="女",age=14)

#默认参数：当调用参数时没有传递参数，就会使用默认缺省参数对应值
def user_info(name,age,gender='男'):
    print(f"姓名是：{name},年龄是：{age},性别是：{gender}")
user_info("小甜",18)
user_info("小甜",18,gender='女')#设置默认值必须在最后

#不定长参数：当调用函数时不确定参数个数时，可以使用不定长参数

#不定长-位置不定长，*号
#不定长定义的形式参数会作为元组存在，接收不定长参数的参数传入
def user_info(*args):
    print(f"args参数的类型是{type(args)}，内容是：{args}")
user_info(1,2,3,'小明',"男孩")

#不定长-关键字不定长，**号
def user_info(**kwargs):
    print(f"args参数的类型是{type(kwargs)}，内容是：{kwargs}")
user_info(name='小王',age=11,gender='男孩',addr='北京')

 
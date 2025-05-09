#定义一个函数，接受另一个函数作为传入参数
def test_fucn(compute):
    result=compute(1,2)#确定computer是函数
    print(type(compute))
    print(f'计算结果是：{result}')
#定义一个函数，准备作为参数传入另一个函数
def compute(x,y):
    return x+y
test_fucn(compute)
#将函数传入的作用是：传入计算逻辑，而非传入数据

#lambda函数
def test_func(compute):
    result=compute(1,2)
    print(f"结果是：{result}")
test_func(lambda x,y:x+y)


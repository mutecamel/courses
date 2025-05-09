#演示使用多个变量接受返回值
def tesy_return():
    return 1,"hello",True
x,y,z=tesy_return()
print(x)
print(y)
print(z)
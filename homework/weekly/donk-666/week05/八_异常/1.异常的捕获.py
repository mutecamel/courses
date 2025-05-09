#基本捕获语法
try:
    f=open('D:/ABC.txt',"r",encoding='UTF-8')
except:
    print("出现异常，文件不存在，将open模式转化为w模式打开")
    f=open('D:/ABC.txt',"w",encoding='UTF-8')
#捕获指定的异常
try:
    print(name)
    #1/0
except NameError as e:
    print('出现变量未被定义的异常')
    print(e)
#捕获多个异常
try:
    print(name)
except(NameError,ZeroDivisionError) as e:
    print('出现了变量未定义 或者 除以0的异常')

#捕获所有的异常
try:
    print('hello')

except Exception as e:
    print("出现异常了")
else:
    print('好高兴，没有异常')

#finally 表示无论如何都要执行异常的代码，例如关闭文件
try:
    open('D:/123.TXT','r',encoding='UTF-8')
except Exception as e:
    print("出现异常了")
else:
    print('好高兴，没有异常')
finally:
    print('我是finally，没有异常我也要异常')
    f.close()

import time
f=open("D:/test.txt", "w", encoding='UTF-8')
f.write("hello world")#将内容写到内存中，而不是硬盘中
f.flush()
#close
f.close()
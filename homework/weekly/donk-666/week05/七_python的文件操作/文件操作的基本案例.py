#打开文件得到文件对象，准备读取
fr=open("D:/bill,txt",'r',encoding='UTF-8')
fw=open('D:/bill.txt.bak','w',encoding='UTF-8')
#for循环读取文件
for line in fr:
    line=line.strip()
    if line.split(",")[4]=='测试':
        continue
    #将内容写出去
    fw.write(line) #continue进入下一次循环，这一次后面的内容就跳过了
    #由于前面对内容进行了strip()的操作，所以要手动的写出换行符
    fw.write("\n")
fr.close()
fw.close()
# 假设这是你的文件读取和统计代码的一部分
# 注意使用双反斜杠或原始字符串
with open("E:\\Desktop\\word.txt", "r", encoding='UTF-8') as file:
    text = file.read()  # 读取整个文件内容

# 使用str.count()方法来统计"itheima"出现的次数
itheima_count = text.count("itheima")

# 打印结果，注意f-string的闭括号
print(f"itheima出现的次数: {itheima_count}")


# 读取contacts.txt文件
with open('contacts.txt', 'r', encoding='utf-8') as file:  # ▼保留字(with/as)、函数调用(open)、字面值(str)、编码参数
    lines = file.readlines()  # ▼对象方法调用(readlines)、语句

# 提取信息并构建邮件内容
emails_data = []  # ▼全局变量、列表字面值
for line in lines:  # ▼保留字(for/in)、循环语句
    parts = line.strip().split()  # ▼字符串方法(strip/split)、运算符(.)、局部变量
    if len(parts) >= 3:  # ▼保留字(if)、比较运算符(>=)、整数字面值
        name = parts[0]  # ▼列表索引([])
        gender = parts[1]
        email = parts[-1]  # ▼负索引
        # 确定称呼（先生/女士）
        title = "先生" if gender == "男" else "女士"  # ▼三元表达式、字符串字面值
        emails_data.append({  # ▼字典字面值、方法调用(append)
            'email': email,
            'name': name,
            'title': title
        })

# 按要求排序
sorted_emails = sorted(emails_data,  # ▼函数调用(sorted)、全局变量
                      key=lambda x: (x['email'].split('@')[1], x['email'].split('@')[0]))  # ▼lambda表达式、形参(x)、元组字面值

# 构建邮件内容并写入文件
with open('emails.txt', 'w', encoding='utf-8') as file:
    for data in sorted_emails:
        email_content = f"""to: <{data['email']}>
尊敬的{data['name']}{data['title']}，您的会员资格即将到期，请及时续费。
---
"""  # ▼f-string格式化、字典键访问
        file.write(email_content)  # ▼方法调用(write)

print("处理完成，结果已保存到emails.txt")  # ▼函数调用(print)

# 未明确出现的概念注释：
# 1. 显式return语句
def add(a, b):
    return a + b  # ▼函数定义中明确返回计算结果

# 2. 显式类型转换
num_str = "123"
num_int = int(num_str)  # ▼将字符串显式转为整数

# 3. 元组字面值
coordinates = (40.7128, 74.0060)  # ▼用圆括号创建不可变序列

# 4. LEGB规则完整示例
x = "全局变量"
def test():
    x = "局部变量"        # ▼局部作用域覆盖全局
    print(x)            # 输出"局部变量"
test()

# 5. 对象属性访问
class Dog:
    def __init__(self, name):
        self.name = name  # ▼定义对象属性
my_dog = Dog("阿黄")
print(my_dog.name)       # ▼访问实例属性
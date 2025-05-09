# 打开 contacts.txt 文件进行读取
with open('contacts.txt', 'r', encoding='utf-8') as file:
    # 读取文件的每一行并去除首尾空格
    lines = file.read().splitlines()

contacts = []
# 遍历每一行数据
for line in lines:
    # 按空格分割每一行，得到姓名、性别和邮箱
    name, gender, email = line.split()
    # 将联系人信息存储为元组
    contacts.append((name, gender, email))

# 定义排序函数，先按邮箱域名排序，再按邮箱用户名排序
def sort_key(contact):
    email = contact[2]
    username, domain = email.split('@')
    return (domain, username)

# 对联系人列表进行排序
contacts.sort(key=sort_key)

# 打开 emails.txt 文件进行写入
with open('emails.txt', 'w', encoding='utf-8') as file:
    # 遍历排序后的联系人列表
    for name, gender, email in contacts:
        # 根据性别生成称呼
        title = '先生' if gender == '男' else '女士'
        # 生成通知内容
        message = f"to: <{email}>\n尊敬的{name}{title}，您的会员资格即将到期，请及时续费。\n---\n"
        # 将通知内容写入文件
        file.write(message)

print("emails.txt 文件已生成。")
# 读取 contacts.txt 文件
contacts = []
try:
    with open('contacts.txt', 'r', encoding='utf-8') as file:
        for line in file:
            name, gender, email = line.strip().split()
            contacts.append((name, gender, email))
except FileNotFoundError:
    print("未找到 contacts.txt 文件，请检查文件路径。")
    exit()

# 按邮箱域名和用户名排序
contacts.sort(key=lambda x: (x[2].split('@')[1], x[2].split('@')[0]))

# 生成邮件内容
email_content = []
for name, gender, email in contacts:
    title = "先生" if gender == "男" else "女士"
    email_content.append(f"to: <{email}>")
    email_content.append(f"尊敬的{name}{title}，您的会员资格即将到期，请及时续费。")
    email_content.append("---")

# 去掉最后一个多余的分隔符
if email_content:
    email_content.pop()

# 写入 emails.txt 文件
try:
    with open('emails.txt', 'w', encoding='utf-8') as file:
        for line in email_content:
            file.write(line + '\n')
    print("已成功生成 emails.txt 文件。")
except Exception as e:
    print(f"写入文件时出现错误: {e}")
    
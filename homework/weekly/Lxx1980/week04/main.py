# 读取联系人数据并处理
contacts_list = []
with open('contacts.txt', 'r', encoding='utf-8') as f:
    for line in f:
        name, gender, email = line.strip().split()
        username, domain = email.split('@')
        contacts_list.append((domain, username, name, gender, email))

# 按域名和用户名排序
sorted_contacts = sorted(contacts_list)

# 生成输出内容
output = []
for contact in sorted_contacts:
    domain, username, name, gender, email = contact
    salutation = '女士' if gender == '女' else '先生'
    block = f"to: <{email}>\n尊敬的{name}{salutation}，您的会员资格即将到期，请及时续费。\n---\n"
    output.append(block)

# 写入到emails.txt文件
with open('emails.txt', 'w', encoding='utf-8') as f:
    f.writelines(output)
    
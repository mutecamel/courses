# 指定绝对路径
contacts_path = r'C:\Users\25231\Desktop\计算机语言\week04\contacts.txt'

# 读取联系人数据
contacts = []
with open(contacts_path, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if line:
            name, gender, email = line.split()
            contacts.append((name, gender, email))

# 定义排序规则：先域名（126.com 优先），再用户名升序
def sort_key(contact):
    username, domain = contact[2].split('@')
    domain_priority = 0 if domain == '126.com' else 1
    return (domain_priority, username)

# 排序联系人
sorted_contacts = sorted(contacts, key=sort_key)

# 生成邮件内容
email_blocks = []
for contact in sorted_contacts:
    name, gender, email = contact
    suffix = '女士' if gender == '女' else '先生'
    block = f"to: <{email}>\n尊敬的{name}{suffix}，您的会员资格即将到期，请及时续费。\n---\n"
    email_blocks.append(block)

# 写入 emails.txt
with open(emails_path, 'w', encoding='utf-8') as f:
    content = ''.join(email_blocks).rstrip('\n') + '\n'
    f.write(content)
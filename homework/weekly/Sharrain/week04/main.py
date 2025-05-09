# 读取contacts.txt文件
with open('contacts.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# 提取信息并构建邮件内容
emails_data = []
for line in lines:
    parts = line.strip().split()
    if len(parts) >= 3:
        name = parts[0]
        gender = parts[1]
        email = parts[-1]
        # 确定称呼（先生/女士）
        title = "先生" if gender == "男" else "女士"
        emails_data.append({
            'email': email,
            'name': name,
            'title': title
        })

# 按要求排序：先按域名排序，再按用户名排序
sorted_emails = sorted(emails_data, key=lambda x: (x['email'].split('@')[1], x['email'].split('@')[0]))

# 构建邮件内容并写入到emails.txt文件
with open('emails.txt', 'w', encoding='utf-8') as file:
    for data in sorted_emails:
        email_content = f"""to: <{data['email']}>
尊敬的{data['name']}{data['title']}，您的会员资格即将到期，请及时续费。
---
"""
        file.write(email_content)

print("处理完成，结果已保存到emails.txt")
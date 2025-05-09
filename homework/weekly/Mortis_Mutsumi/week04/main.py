# 读取联系人信息并处理
contacts = []
with open("contacts.txt", "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        parts = line.split()
        if len(parts) != 3:
            continue  # 跳过格式不正确的行
        name, gender, email = parts
        # 分割邮箱为用户名和域名
        try:
            username, domain = email.split("@")
        except ValueError:
            continue  # 邮箱格式错误，跳过
        contacts.append(
            {
                "name": name,
                "gender": gender,
                "email": email,
                "username": username,
                "domain": domain,
            }
        )

# 排序：先按域名，再按用户名
sorted_contacts = sorted(contacts, key=lambda x: (x["domain"], x["username"]))

# 生成邮件内容
lines = []
for contact in sorted_contacts:
    salutation = "先生" if contact["gender"] == "男" else "女士"
    lines.append(f"to: <{contact['email']}>")
    lines.append(
        f"尊敬的{contact['name']}{salutation}，您的会员资格即将到期，请及时续费。"
    )
    lines.append("---")

content = "\n".join(lines)

# 写入emails.txt
with open("emails.txt", "w", encoding="utf-8") as f:
    f.write(content)

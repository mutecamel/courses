# 读取联系人文件
with open("contacts.txt", "r", encoding="utf-8") as f:
    contacts = [line.strip().split() for line in f if line.strip()]

# 处理数据：将联系人信息转换为字典列表并提取邮箱域名和用户名
processed_contacts = []
for name, gender, email in contacts:
    username, domain = email.split("@")
    processed_contacts.append(
        {
            "name": name,
            "gender": gender,
            "email": email,
            "domain": domain,
            "username": username,
        }
    )

# 排序：先按域名排序（126.com在前），然后按用户名排序
processed_contacts.sort(key=lambda x: (x["domain"], x["username"]))

# 生成邮件内容并写入emails.txt
with open("emails.txt", "w", encoding="utf-8") as f:
    for contact in processed_contacts:
        # 根据性别确定称呼
        title = "女士" if contact["gender"] == "女" else "先生"
        email_content = f"""to: <{contact["email"]}>
尊敬的{contact["name"]}{title}，您的会员资格即将到期，请及时续费。
---
"""
        f.write(email_content)

print("邮件内容已成功生成到emails.txt文件")

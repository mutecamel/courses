# 读取contacts.txt文件内容
contacts = []
with open("contacts.txt", "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if line:
            name, gender, email = line.split()
            contacts.append({"name": name, "gender": gender, "email": email})

# 按邮箱域名和用户名排序
sorted_contacts = sorted(
    contacts, key=lambda x: (x["email"].split("@")[1], x["email"].split("@")[0])
)

# 生成输出内容
output_lines = []
for i, contact in enumerate(sorted_contacts):
    # 根据性别确定称呼
    title = "女士" if contact["gender"] == "女" else "先生"
    # 添加邮件内容行
    output_lines.append(f"to: <{contact['email']}>")
    output_lines.append(
        f"尊敬的{contact['name']}{title}，您的会员资格即将到期，请及时续费。"
    )
    # 如果不是最后一个联系人，添加分隔符
    if i != len(sorted_contacts) - 1:
        output_lines.append("---")

# 写入emails.txt文件
with open("emails.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(output_lines))

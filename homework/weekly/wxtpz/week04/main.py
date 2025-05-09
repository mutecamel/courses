# 读取 contacts.txt 文件
try:
    with open("contacts.txt", "r", encoding="utf-8") as file:
        contacts = []
        for line in file:
            name, gender, email = line.strip().split()
            contacts.append((name, gender, email))
except FileNotFoundError:
    print("错误：未找到 contacts.txt 文件。")
    exit()

# 按邮箱域名和用户名排序
sorted_contacts = sorted(
    contacts, key=lambda x: (x[2].split("@")[1], x[2].split("@")[0])
)

# 生成邮件内容
email_content = []
for name, gender, email in sorted_contacts:
    title = "先生" if gender == "男" else "女士"
    email_text = (
        f"to: <{email}>\n尊敬的{name}{title}，您的会员资格即将到期，请及时续费。\n---"
    )
    email_content.append(email_text)

# 输出到 emails.txt 文件
try:
    with open("emails.txt", "w", encoding="utf-8") as output_file:
        output_file.write("\n".join(email_content).rstrip("---"))
    print("邮件内容已成功写入 emails.txt 文件。")
except Exception as e:
    print(f"错误：写入文件时出现问题 - {e}")

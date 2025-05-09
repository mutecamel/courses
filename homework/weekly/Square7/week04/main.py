try:
    # 读取联系人文件
    with open("contacts.txt", "r", encoding="utf-8") as file:
        contacts = file.readlines()

    # 解析联系人信息
    parsed_contacts = []
    for contact in contacts:
        name, gender, email = contact.strip().split(" ")
        parsed_contacts.append((name, gender, email))

    # 按邮箱域名和用户名排序
    parsed_contacts.sort(key=lambda x: (x[2].split("@")[1], x[2].split("@")[0]))

    # 生成邮件内容
    email_content = ""
    for name, gender, email in parsed_contacts:
        title = "先生" if gender == "男" else "女士"
        email_content += f"to: <{email}>\n"
        email_content += f"尊敬的{name}{title}，您的会员资格即将到期，请及时续费。\n"
        email_content += "---\n"

    # 写入emails.txt文件
    with open("emails.txt", "w", encoding="utf-8") as file:
        file.write(email_content)

    print("邮件内容已成功写入emails.txt文件。")
except FileNotFoundError:
    print("错误: contacts.txt文件未找到。")
except Exception as e:
    print(f"发生未知错误: {e}")

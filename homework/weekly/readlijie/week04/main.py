def process_contacts(input_file, output_file):
    # 读取 contacts.txt 文件
    with open(input_file, "r", encoding="utf-8") as file:
        lines = file.readlines()

    # 解析联系人信息
    contacts = []
    for line in lines:
        name, gender, email = line.strip().split()
        contacts.append((name, gender, email))

    # 按邮箱域名和用户名排序
    contacts.sort(key=lambda x: (x[2].split("@")[1], x[2].split("@")[0]))

    # 生成邮件内容
    with open(output_file, "w", encoding="utf-8") as file:
        for name, gender, email in contacts:
            # 根据性别选择称呼
            if gender == "男":
                title = "先生"
            else:
                title = "女士"
            # 写入邮件内容
            file.write(f"to: <{email}>\n")
            file.write(f"尊敬的{name}{title}，您的会员资格即将到期，请及时续费。\n")
            file.write("---\n")


# 调用函数处理文件
process_contacts("contacts.txt", "emails.txt")

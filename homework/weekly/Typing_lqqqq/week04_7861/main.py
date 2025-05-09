try:
    # 读取 contacts.txt 文件
    with open("contacts.txt", "r", encoding="utf-8") as file:
        contacts = []
        for line in file:
            name, gender, email = line.strip().split()
            contacts.append((name, gender, email))

    # 按邮箱域名和用户名排序
    contacts.sort(key=lambda x: (x[2].split("@")[1], x[2].split("@")[0]))

    # 生成邮件内容
    email_content = []
    for name, gender, email in contacts:
        title = "先生" if gender == "男" else "女士"
        message = f"to: <{email}>\n尊敬的{name}{title}，您的会员资格即将到期，请及时续费。\n---"
        email_content.append(message)

    # 去除最后一个多余的分隔符
    if email_content:
        email_content[-1] = email_content[-1].rstrip("---")

    # 写入 emails.txt 文件
    with open("emails.txt", "w", encoding="utf-8") as out_file:
        out_file.write("\n".join(email_content))

except FileNotFoundError:
    print("未找到 contacts.txt 文件，请检查文件是否存在。")
except ValueError:
    print("contacts.txt 文件格式有误，请确保每行包含姓名、性别和邮箱，用空格分隔。")

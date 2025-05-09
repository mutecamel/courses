def process_contacts():
    try:
        # 读取联系人文件
        with open("contacts.txt", "r", encoding="utf-8") as file:
            contacts = file.readlines()

        # 处理联系人信息
        processed_contacts = []
        for contact in contacts:
            name, gender, email = contact.strip().split()
            processed_contacts.append((name, gender, email))

        # 按邮箱域名和用户名排序
        processed_contacts.sort(key=lambda x: (x[2].split("@")[1], x[2].split("@")[0]))

        # 生成邮件内容
        emails = []
        for name, gender, email in processed_contacts:
            title = "先生" if gender == "男" else "女士"
            email_content = f"to: <{email}>\n尊敬的{name}{title}，您的会员资格即将到期，请及时续费。\n---"
            emails.append(email_content)

        # 写入邮件文件
        with open("emails.txt", "w", encoding="utf-8") as file:
            file.write("\n".join(emails).rstrip("---"))

    except FileNotFoundError:
        print("错误: contacts.txt 文件未找到!")
    except Exception as e:
        print(f"错误: 发生了一个未知错误: {e}")


if __name__ == "__main__":
    process_contacts()

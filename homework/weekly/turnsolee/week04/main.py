def process_contacts():
    try:
        # 读取联系人文件
        with open("contacts.txt", "r", encoding="utf-8") as file:
            contacts = file.readlines()

        contact_list = []
        for contact in contacts:
            name, gender, email = contact.strip().split()
            contact_list.append((name, gender, email))

        # 按邮箱域名和用户名排序
        contact_list.sort(key=lambda x: (x[2].split("@")[1], x[2].split("@")[0]))

        # 生成邮件内容
        email_content = []
        for name, gender, email in contact_list:
            title = "先生" if gender == "男" else "女士"
            email_content.append(f"to: <{email}>")
            email_content.append(
                f"尊敬的{name}{title}，您的会员资格即将到期，请及时续费。"
            )
            email_content.append("---")

        # 去除最后一个多余的分隔符
        if email_content:
            email_content.pop()

        # 写入邮件文件
        with open("emails.txt", "w", encoding="utf-8") as file:
            file.write("\n".join(email_content))

        print("邮件文件生成成功！")
    except FileNotFoundError:
        print("错误：未找到 contacts.txt 文件。")
    except Exception as e:
        print(f"发生未知错误：{e}")


if __name__ == "__main__":
    process_contacts()

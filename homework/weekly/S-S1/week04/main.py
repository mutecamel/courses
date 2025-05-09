def process_contacts():
    try:
        # 读取联系人文件
        with open("contacts.txt", "r", encoding="utf-8") as file:
            contacts = file.readlines()

        # 处理联系人信息
        processed_contacts = []
        for contact in contacts:
            name, gender, email = contact.strip().split()
            title = "先生" if gender == "男" else "女士"
            processed_contacts.append((email, name, title))

        # 按邮箱域名和用户名排序
        processed_contacts.sort(key=lambda x: (x[0].split("@")[1], x[0].split("@")[0]))

        # 生成邮件内容
        emails_content = []
        for email, name, title in processed_contacts:
            email_content = f"to: <{email}>\n"
            email_content += (
                f"尊敬的{name}{title}，您的会员资格即将到期，请及时续费。\n---\n"
            )
            emails_content.append(email_content)

        # 写入 emails.txt 文件
        with open("emails.txt", "w", encoding="utf-8") as file:
            file.writelines(emails_content)

        print("邮件提醒文件生成成功！")
    except FileNotFoundError:
        print("错误：未找到 contacts.txt 文件，请检查文件路径。")
    except Exception as e:
        print(f"发生未知错误：{e}")


if __name__ == "__main__":
    process_contacts()

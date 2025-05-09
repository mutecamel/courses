def process_contacts():
    try:
        # 读取 contacts.txt 文件
        with open("contacts.txt", "r", encoding="utf-8") as file:
            contacts = file.readlines()

        # 解析联系人信息
        parsed_contacts = []
        for contact in contacts:
            name, gender, email = contact.strip().split()
            parsed_contacts.append((name, gender, email))

        # 按邮箱域名和用户名排序
        sorted_contacts = sorted(
            parsed_contacts, key=lambda x: (x[2].split("@")[1], x[2].split("@")[0])
        )

        # 生成邮件内容
        email_content = []
        for name, gender, email in sorted_contacts:
            title = "先生" if gender == "男" else "女士"
            email_content.append(
                f"to: <{email}>\n尊敬的{name}{title}，您的会员资格即将到期，请及时续费。\n---"
            )

        # 去除最后一个多余的 ---
        if email_content:
            email_content[-1] = email_content[-1].rstrip("---")

        # 写入 emails.txt 文件
        with open("emails.txt", "w", encoding="utf-8") as file:
            file.write("\n".join(email_content))

        print("邮件通知文件生成成功！")
    except FileNotFoundError:
        print("错误：未找到 contacts.txt 文件！")
    except Exception as e:
        print(f"发生未知错误：{e}")


if __name__ == "__main__":
    process_contacts()

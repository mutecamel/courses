# 定义一个函数来处理联系人信息
def process_contacts():
    try:
        # 读取 contacts.txt 文件
        with open("contacts.txt", "r", encoding="utf-8") as file:
            contacts = file.readlines()

        # 初始化一个空列表来存储联系人信息
        contact_list = []
        for contact in contacts:
            # 分割每行内容
            name, gender, email = contact.strip().split()
            # 将联系人信息存储为元组
            contact_list.append((name, gender, email))

        # 按邮箱域名和用户名排序
        sorted_contacts = sorted(
            contact_list, key=lambda x: (x[2].split("@")[1], x[2].split("@")[0])
        )

        # 初始化一个空字符串来存储邮件内容
        email_content = ""
        for name, gender, email in sorted_contacts:
            # 根据性别生成称呼
            title = "先生" if gender == "男" else "女士"
            # 拼接邮件内容
            email_content += f"to: <{email}>\n"
            email_content += (
                f"尊敬的{name}{title}，您的会员资格即将到期，请及时续费。\n"
            )
            email_content += "---\n"

        # 写入 emails.txt 文件
        with open("emails.txt", "w", encoding="utf-8") as file:
            file.write(email_content.rstrip("---\n"))

    except FileNotFoundError:
        print("错误: contacts.txt 文件未找到。")
    except Exception as e:
        print(f"发生未知错误: {e}")


if __name__ == "__main__":
    process_contacts()

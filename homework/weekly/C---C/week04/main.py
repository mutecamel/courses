def read_contacts(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            lines = file.readlines()
            contacts = []
            for line in lines:
                name, gender, email = line.strip().split()
                contacts.append((name, gender, email))
            return contacts
    except FileNotFoundError:
        print("错误: 未找到联系人文件！")
        return []


def generate_emails(contacts):
    sorted_contacts = sorted(
        contacts, key=lambda x: (x[2].split("@")[1], x[2].split("@")[0])
    )
    emails = []
    for name, gender, email in sorted_contacts:
        title = "先生" if gender == "男" else "女士"
        email_text = f"to: <{email}>\n尊敬的{name}{title}，您的会员资格即将到期，请及时续费。\n---"
        emails.append(email_text)
    return "\n".join(emails)


def write_emails(file_path, content):
    try:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(content)
    except Exception as e:
        print(f"错误: 写入邮件文件时出错: {e}")


if __name__ == "__main__":
    contacts = read_contacts("contacts.txt")
    if contacts:
        email_content = generate_emails(contacts)
        write_emails("emails.txt", email_content)
        print("邮件内容已成功写入 emails.txt 文件。")

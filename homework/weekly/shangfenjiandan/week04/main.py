def read_contacts(file_path):
    contacts = []
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                name, gender, email = line.strip().split()
                contacts.append((name, gender, email))
    except FileNotFoundError:
        print(f"错误：未找到文件 {file_path}。")
    return contacts


def generate_emails(contacts):
    sorted_contacts = sorted(
        contacts, key=lambda x: (x[2].split("@")[1], x[2].split("@")[0])
    )
    email_text = ""
    for name, gender, email in sorted_contacts:
        title = "先生" if gender == "男" else "女士"
        email_text += f"to: <{email}>\n"
        email_text += f"尊敬的{name}{title}，您的会员资格即将到期，请及时续费。\n"
        email_text += "---\n"
    return email_text


def write_emails(file_path, email_text):
    try:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(email_text)
        print(f"邮件内容已成功写入 {file_path}。")
    except Exception as e:
        print(f"错误：写入文件 {file_path} 时出现问题：{e}。")


if __name__ == "__main__":
    contacts = read_contacts("contacts.txt")
    if contacts:
        email_text = generate_emails(contacts)
        write_emails("emails.txt", email_text)

def read_contacts(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            contacts = []
            for line in file:
                name, gender, email = line.strip().split()
                contacts.append((name, gender, email))
        return contacts
    except FileNotFoundError:
        print(f"错误：未找到文件 {file_path}。")
        return []


def generate_emails(contacts):
    sorted_contacts = sorted(contacts, key=lambda x: (x[2].split('@')[1], x[2].split('@')[0]))
    email_content = []
    for name, gender, email in sorted_contacts:
        title = "先生" if gender == "男" else "女士"
        email_text = f"to: <{email}>\n尊敬的{name}{title}，您的会员资格即将到期，请及时续费。\n---"
        email_content.append(email_text)
    return "\n".join(email_content).rstrip('---')


def write_emails(file_path, content):
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"邮件已成功写入 {file_path}。")
    except Exception as e:
        print(f"错误：写入文件 {file_path} 时出错 - {e}。")


if __name__ == "__main__":
    contacts = read_contacts('contacts.txt')
    if contacts:
        emails = generate_emails(contacts)
        write_emails('emails.txt', emails)
    
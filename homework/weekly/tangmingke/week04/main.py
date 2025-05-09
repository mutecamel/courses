def read_contacts(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            contacts = []
            for line in file:
                name, gender, email = line.strip().split()
                contacts.append((name, gender, email))
            return contacts
    except FileNotFoundError:
        print("错误: 未找到联系人文件!")
        return []


def generate_emails(contacts):
    emails = []
    for name, gender, email in sorted(contacts, key=lambda x: (x[2].split('@')[1], x[2].split('@')[0])):
        title = "先生" if gender == "男" else "女士"
        email_content = f"to: <{email}>\n尊敬的{name}{title}，您的会员资格即将到期，请及时续费。\n---"
        emails.append(email_content)
    return emails


def write_emails(emails, output_file):
    try:
        with open(output_file, 'w', encoding='utf-8') as file:
            for email in emails:
                file.write(email + '\n')
    except Exception as e:
        print(f"错误: 写入文件时出现问题: {e}")


if __name__ == "__main__":
    contacts = read_contacts('contacts.txt')
    if contacts:
        emails = generate_emails(contacts)
        write_emails(emails, 'emails.txt')
        print("邮件已成功生成并保存到 emails.txt 文件中。")
    
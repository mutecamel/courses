def read_contacts(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            contacts = []
            for line in file:
                name, gender, email = line.strip().split()
                contacts.append((name, gender, email))
        return contacts
    except FileNotFoundError:
        print(f"错误: 文件 {file_path} 未找到。")
        return []
    except Exception as e:
        print(f"错误: 读取文件时发生未知错误: {e}")
        return []


def generate_emails(contacts):
    sorted_contacts = sorted(contacts, key=lambda x: (x[2].split('@')[1], x[2].split('@')[0]))
    emails = []
    for name, gender, email in sorted_contacts:
        title = "先生" if gender == "男" else "女士"
        email_content = f"to: <{email}>\n尊敬的{name}{title}，您的会员资格即将到期，请及时续费。\n---"
        emails.append(email_content)
    return "\n".join(emails)


def write_emails(emails, output_file):
    try:
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(emails)
        print(f"邮件已成功写入 {output_file}。")
    except Exception as e:
        print(f"错误: 写入文件时发生未知错误: {e}")


if __name__ == "__main__":
    contacts_file = 'contacts.txt'
    output_file = 'emails.txt'
    contacts = read_contacts(contacts_file)
    if contacts:
        emails = generate_emails(contacts)
        write_emails(emails, output_file)
    
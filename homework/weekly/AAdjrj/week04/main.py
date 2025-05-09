def read_contacts(file_path):
    try:
        contacts = []
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                parts = line.strip().split()
                if len(parts) == 3:
                    name, gender, email = parts
                    contacts.append((name, gender, email))
        return contacts
    except FileNotFoundError:
        print(f"错误: 文件 {file_path} 未找到。")
        return []
    except Exception as e:
        print(f"错误: 读取文件时发生未知错误: {e}")
        return []


def generate_emails(contacts):
    emails = []
    for name, gender, email in contacts:
        title = "先生" if gender == "男" else "女士"
        email_content = f"to: <{email}>\n尊敬的 {name}{title}，您的会员资格即将到期，请及时续费。\n---"
        emails.append(email_content)
    return emails


def sort_contacts(contacts):
    def sort_key(contact):
        _, _, email = contact
        username, domain = email.split("@")
        return (domain, username)

    return sorted(contacts, key=sort_key)


def write_emails(emails, output_file):
    try:
        with open(output_file, "w", encoding="utf-8") as file:
            for email in emails:
                file.write(email + "\n")
    except Exception as e:
        print(f"错误: 写入文件 {output_file} 时发生未知错误: {e}")


if __name__ == "__main__":
    contacts = read_contacts("contacts.txt")
    sorted_contacts = sort_contacts(contacts)
    emails = generate_emails(sorted_contacts)
    write_emails(emails, "emails.txt")
    print("邮件通知已生成并保存到 emails.txt 文件中。")

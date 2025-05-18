def read_contacts(file_path):
    contacts = []
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                parts = line.strip().split()
                if len(parts) == 3:
                    name, gender, email = parts
                    contacts.append((name, gender, email))
    except FileNotFoundError:
        print(f"错误: 未找到 {file_path} 文件。")
    return contacts


def generate_emails(contacts):
    emails = []
    for name, gender, email in contacts:
        title = "先生" if gender == "男" else "女士"
        email_text = f"to: <{email}>\n尊敬的{name}{title}，您的会员资格即将到期，请及时续费。\n---"
        emails.append(email_text)
    return emails


def sort_contacts(contacts):
    def custom_sort_key(item):
        email = item[2]
        domain = email.split("@")[1]
        username = email.split("@")[0]
        return (domain, username)

    return sorted(contacts, key=custom_sort_key)


def write_emails(emails, output_file):
    try:
        with open(output_file, "w", encoding="utf-8") as file:
            for email in emails:
                file.write(email + "\n")
    except Exception as e:
        print(f"写入 {output_file} 文件时出错: {e}")


if __name__ == "__main__":
    contacts = read_contacts("contacts.txt")
    sorted_contacts = sort_contacts(contacts)
    emails = generate_emails(sorted_contacts)
    write_emails(emails, "emails.txt")

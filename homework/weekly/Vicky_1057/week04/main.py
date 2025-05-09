def read_contacts(file_path):
    contacts = []
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                name, gender, email = line.strip().split()
                contacts.append((name, gender, email))
    except FileNotFoundError:
        print(f"错误：未找到文件 {file_path}")
    return contacts


def generate_emails(contacts):
    emails = []
    for name, gender, email in contacts:
        title = "先生" if gender == "男" else "女士"
        email_content = f"to: <{email}>\n尊敬的{name}{title}，您的会员资格即将到期，请及时续费。\n---"
        emails.append(email_content)
    return emails


def sort_contacts(contacts):
    return sorted(contacts, key=lambda x: (x[2].split("@")[1], x[2].split("@")[0]))


def write_emails(emails, output_file):
    try:
        with open(output_file, "w", encoding="utf-8") as file:
            for email in emails:
                file.write(email + "\n")
    except Exception as e:
        print(f"写入文件时出错：{e}")


if __name__ == "__main__":
    contacts = read_contacts("contacts.txt")
    sorted_contacts = sort_contacts(contacts)
    emails = generate_emails(sorted_contacts)
    write_emails(emails, "emails.txt")

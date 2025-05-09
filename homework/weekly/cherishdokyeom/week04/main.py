def read_contacts(file_path):
    contacts = []
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                name, gender, email = line.strip().split()
                contacts.append((name, gender, email))
    except FileNotFoundError:
        print("错误: 未找到联系人文件!")
    except Exception as e:
        print(f"错误: 发生了一个未知错误: {e}")
    return contacts


def generate_emails(contacts):
    emails = []
    for name, gender, email in contacts:
        title = "先生" if gender == "男" else "女士"
        email_text = f"to: <{email}>\n尊敬的{name}{title}，您的会员资格即将到期，请及时续费。\n---"
        emails.append(email_text)
    return emails


def sort_emails(emails):
    def get_sort_key(email):
        start = email.find("<") + 1
        end = email.find(">")
        email_addr = email[start:end]
        username, domain = email_addr.split("@")
        return (domain, username)

    return sorted(emails, key=get_sort_key)


def write_emails(emails, output_file):
    try:
        with open(output_file, "w", encoding="utf-8") as file:
            for email in emails:
                file.write(email + "\n")
    except Exception as e:
        print(f"错误: 写入文件时发生错误: {e}")


if __name__ == "__main__":
    contacts = read_contacts("contacts.txt")
    if contacts:
        emails = generate_emails(contacts)
        sorted_emails = sort_emails(emails)
        write_emails(sorted_emails, "emails.txt")
        print("邮件提醒已生成并排序输出到 emails.txt 文件。")

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
        print("错误：未找到 contacts.txt 文件。")
        return []
    except Exception as e:
        print(f"发生未知错误：{e}")
        return []


def sort_contacts(contacts):
    return sorted(contacts, key=lambda x: (x[2].split("@")[1], x[2].split("@")[0]))


def generate_email_content(contacts):
    email_content = []
    for name, gender, email in contacts:
        title = "先生" if gender == "男" else "女士"
        email_text = f"to: <{email}>\n尊敬的{name}{title}，您的会员资格即将到期，请及时续费。\n---"
        email_content.append(email_text)
    return email_content


def write_emails_to_file(email_content, output_file_path):
    try:
        with open(output_file_path, "w", encoding="utf-8") as output_file:
            output_file.write("\n".join(email_content).rstrip("---"))
        print("邮件内容已成功写入 emails.txt 文件。")
    except Exception as e:
        print(f"写入文件时发生错误：{e}")


def generate_emails():
    contacts = read_contacts("contacts.txt")
    if contacts:
        sorted_contacts = sort_contacts(contacts)
        email_content = generate_email_content(sorted_contacts)
        write_emails_to_file(email_content, "emails.txt")


if __name__ == "__main__":
    generate_emails()

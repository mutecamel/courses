def read_contacts(filename):
    """读取联系人文件并返回联系人列表"""
    contacts = []
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            # 去除空白字符并分割字段
            line = line.strip()
            if not line:
                continue
            name, gender, email = line.split()
            contacts.append({"name": name, "gender": gender, "email": email})
    return contacts


def sort_contacts(contacts):
    """对联系人列表进行排序"""

    def get_sort_key(contact):
        # 先按域名排序，再按用户名排序
        username, domain = contact["email"].split("@")
        return (domain, username)

    return sorted(contacts, key=get_sort_key)


def generate_email_content(contact):
    """生成单个联系人的邮件内容"""
    gender_title = "女士" if contact["gender"] == "女" else "先生"
    email = contact["email"]
    name = contact["name"]

    content = f"to: <{email}>\n"
    content += f"尊敬的{name}{gender_title}，您的会员资格即将到期，请及时续费。\n"
    content += "---"
    return content


def write_emails(filename, contacts):
    """将邮件内容写入文件"""
    with open(filename, "w", encoding="utf-8") as file:
        for contact in contacts:
            content = generate_email_content(contact)
            file.write(content + "\n")


def main():
    # 读取联系人数据
    contacts = read_contacts("contacts.txt")

    # 对联系人进行排序
    sorted_contacts = sort_contacts(contacts)

    # 生成并写入邮件内容
    write_emails("emails.txt", sorted_contacts)


if __name__ == "__main__":
    main()

# 读取 contacts.txt 文件
def read_contacts(file_path):
    contacts = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                name, gender, email = line.strip().split()
                contacts.append((name, gender, email))
    except FileNotFoundError:
        print(f"错误: 文件 {file_path} 未找到。")
    return contacts

# 对联系人按邮箱域名和用户名排序
def sort_contacts(contacts):
    return sorted(contacts, key=lambda x: (x[2].split('@')[1], x[2].split('@')[0]))

# 生成通知内容并写入 emails.txt 文件
def generate_emails(contacts, output_file):
    try:
        with open(output_file, 'w', encoding='utf-8') as file:
            for name, gender, email in contacts:
                title = "先生" if gender == "男" else "女士"
                message = f"to: <{email}>\n尊敬的{name}{title}，您的会员资格即将到期，请及时续费。\n---\n"
                file.write(message)
    except Exception as e:
        print(f"错误: 写入文件 {output_file} 时出现问题: {e}")

if __name__ == "__main__":
    contacts = read_contacts('contacts.txt')
    sorted_contacts = sort_contacts(contacts)
    generate_emails(sorted_contacts, 'emails.txt')
    
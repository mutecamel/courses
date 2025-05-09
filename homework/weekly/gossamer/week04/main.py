def process_contacts():
    try:
        with open('contacts.txt', 'r', encoding='utf-8') as file:
            contacts = file.readlines()

        contact_list = []
        for contact in contacts:
            parts = contact.strip().split()
            if len(parts) != 3:
                print(f"错误：行 '{contact.strip()}' 格式不正确，跳过此条记录。")
                continue
            name, gender, email = parts
            contact_list.append((name, gender, email))

        contact_list.sort(key=lambda x: (x[2].split('@')[1], x[2].split('@')[0]))

        email_content = []
        for name, gender, email in contact_list:
            title = '先生' if gender == '男' else '女士'
            email_content.extend([
                f'to: <{email}>',
                f'尊敬的{name}{title}，您的会员资格即将到期，请及时续费。',
                '---'
            ])

        if email_content:
            email_content.pop()

        with open('emails.txt', 'w', encoding='utf-8') as file:
            file.write('\n'.join(email_content))

    except FileNotFoundError:
        print("错误：未找到 'contacts.txt' 文件。")
    except Exception as e:
        print(f"发生未知错误：{e}")


if __name__ == "__main__":
    process_contacts()
    
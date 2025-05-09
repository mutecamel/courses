def process_contacts():
    try:
        with open("contacts.txt", "r", encoding="utf-8") as file:
            contacts = file.readlines()

        contact_list = []
        for contact in contacts:
            name, gender, email = contact.strip().split()
            contact_list.append((name, gender, email))

        def sort_key(item):
            email = item[2]
            domain, username = email.split("@")[::-1]
            return (domain, username)

        sorted_contacts = sorted(contact_list, key=sort_key)

        with open("emails.txt", "w", encoding="utf-8") as output_file:
            for name, gender, email in sorted_contacts:
                title = "先生" if gender == "男" else "女士"
                output_file.write(f"to: <{email}>\n")
                output_file.write(
                    f"尊敬的{name}{title}，您的会员资格即将到期，请及时续费。\n"
                )
                output_file.write("---\n")

    except FileNotFoundError:
        print("错误: 未找到 contacts.txt 文件。")
    except Exception as e:
        print(f"发生未知错误: {e}")


if __name__ == "__main__":
    process_contacts()

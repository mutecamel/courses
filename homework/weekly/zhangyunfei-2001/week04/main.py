def process_contacts():
    try:
        with open("contacts.txt", "r", encoding="utf-8") as file:
            contacts = []
            for line in file:
                name, gender, email = line.strip().split()
                contacts.append((name, gender, email))

        contacts.sort(key=lambda x: (x[2].split("@")[1], x[2].split("@")[0]))

        with open("emails.txt", "w", encoding="utf-8") as output_file:
            for name, gender, email in contacts:
                title = "先生" if gender == "男" else "女士"
                output_file.write(f"to: <{email}>\n")
                output_file.write(
                    f"尊敬的{name}{title}，您的会员资格即将到期，请及时续费。\n"
                )
                output_file.write("---\n")
    except FileNotFoundError:
        print("错误: contacts.txt 文件未找到!")
    except Exception as e:
        print(f"错误: 发生了一个未知错误: {e}")


if __name__ == "__main__":
    process_contacts()

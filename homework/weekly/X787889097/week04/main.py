try:
    with open("contacts.txt", "r", encoding="utf-8") as infile:
        lines = infile.readlines()

    contact_info = []
    for line in lines:
        name, gender, email = line.strip().split()
        username, domain = email.split("@")
        salutation = "先生" if gender == "男" else "女士"
        contact_info.append((domain, username, name, salutation, email))

    # 按邮箱域名和用户名排序
    contact_info.sort()

    output_content = []
    for domain, username, name, salutation, email in contact_info:
        output_content.extend(
            [
                f"to: <{email}>",
                f"尊敬的{name}{salutation}，您的会员资格即将到期，请及时续费。",
                "---",
            ]
        )

    with open("emails.txt", "w", encoding="utf-8") as outfile:
        for line in output_content:
            outfile.write(line + "\n")

    print("已完成处理，结果保存于 emails.txt 文件。")
except FileNotFoundError:
    print("未找到 contacts.txt 文件，请检查文件路径与名称。")
except ValueError:
    print("contacts.txt 文件格式有误，每行应包含姓名、性别、邮箱，用空格分隔。")
except Exception as e:
    print(f"出现未知错误：{e}")

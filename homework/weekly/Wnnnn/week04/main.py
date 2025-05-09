import os

# 打印当前工作目录
print(f"当前工作目录: {os.getcwd()}")

try:
    with open("contacts.txt", "r", encoding="utf-8") as file:
        contacts = file.readlines()

    # 处理联系人数据
    processed_contacts = []
    for contact in contacts:
        name, gender, email = contact.strip().split()
        title = "先生" if gender == "男" else "女士"
        processed_contacts.append(
            (email, f"尊敬的{name}{title}，您的会员资格即将到期，请及时续费。")
        )

    # 按邮箱域名和用户名排序
    sorted_contacts = sorted(
        processed_contacts, key=lambda x: (x[0].split("@")[1], x[0].split("@")[0])
    )

    # 生成邮件内容
    email_content = []
    for email, message in sorted_contacts:
        email_content.append(f"to: <{email}>")
        email_content.append(message)
        email_content.append("---")

    # 去除最后一个多余的分隔符
    if email_content:
        email_content.pop()

    # 写入邮件文件
    with open("emails.txt", "w", encoding="utf-8") as file:
        file.write("\n".join(email_content))

except FileNotFoundError:
    print("错误：未找到 contacts.txt 文件。")
except Exception as e:
    print(f"发生未知错误：{e}")

def read_contacts(filename):
    contacts = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            name, gender, email = line.strip().split()
            contacts.append((name, gender, email))
    return contacts

def sort_contacts(contacts):
    # Sort by domain and then by username
    contacts.sort(key=lambda x: (x[2].split('@')[1], x[2].split('@')[0]))
    return contacts

def generate_emails(contacts):
    emails_content = []
    for name, gender, email in contacts:
        if gender == '男':
            gender_title = '先生'
        else:
            gender_title = '女士'
        message = f"to: <{email}>\n尊敬的{name}{gender_title}，您的会员资格即将到期，请及时续费。\n---\n"
        emails_content.append(message)
    return emails_content

def write_emails(emails_content, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        file.writelines(emails_content)

if __name__ == "__main__":
    # Step 1: Read contacts from file
    contacts = read_contacts('contacts.txt')
    
    # Step 2: Sort contacts
    sorted_contacts = sort_contacts(contacts)
    
    # Step 3: Generate email content
    emails_content = generate_emails(sorted_contacts)
    
    # Step 4: Write emails to file
    write_emails(emails_content, 'emails.txt')

    print("Emails have been generated successfully.")
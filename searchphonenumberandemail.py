import re

def search_phone_email(filename):
    # Regular expression patterns
    phone_pattern = r'\+\d{10,15}'      # + followed by 10–15 digits
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

    try:
        with open(filename, "r") as file:
            text = file.read()

        phones = re.findall(phone_pattern, text)
        emails = re.findall(email_pattern, text)

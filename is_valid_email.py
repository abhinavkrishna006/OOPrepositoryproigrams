import re

def is_valid_email(email):
    # Define a regular expression for a basic email pattern
    email_pattern = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')

    # Use the regular expression to match the email pattern
    match = re.match(email_pattern, email)

    # If there's a match, the email is valid; otherwise, it's not valid
    return bool(match)

# Example usage:
email_address = "example@email.com"  # Replace with the email address you want to check
result = is_valid_email(email_address)
print(f"Is the email address {email_address} valid? {result}")

def is_valid_email(email):
    # Rule 1: Must contain at least 1 character before the @ symbol
    if email.find('@') == 0:
        return False

    # Rule 2: Must contain the @ symbol
    if '@' not in email:
        return False

    # Rule 3: Must have at least 1 character after the last period (.)
    if email.rfind('.') == len(email) - 1:
        return False

    # Rule 4: Must contain at least 1 character after the last period (.)
    if email[email.rfind('.') + 1:] == '':
        return False

    # Rule 5: Maximum 256 characters
    if len(email) > 256:
        return False

    # Rule 6: Must start with a letter or a number
    if not (email[0].isalpha() or email[0].isdigit()):
        return False

    # If all rules pass, the email is valid
    return True

# Example usage:
email_address = "example@email.com"  # Replace with the email address you want to check
result = is_valid_email(email_address)
print(f"Is the email address {email_address} valid? {result}")


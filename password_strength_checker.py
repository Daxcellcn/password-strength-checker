import re

def is_strong_password(password):
    # Check length (at least 8 characters)
    if len(password) < 8:
        return False

    # Check for uppercase, lowercase, numbers, and special characters
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = bool(re.search(r'[!@#\$%^&*()_+{}:;<>,.?~\\-]', password))

    # Check for common words (you can add more words to this list)
    common_words = ['password', '123456', 'qwerty', 'letmein']
    if any(word in password.lower() for word in common_words):
        return False

    # Password is considered strong if it meets all criteria
    return has_upper and has_lower and has_digit and has_special

# Input a password to check
password = input("Enter a password: ")

if is_strong_password(password):
    print("Strong password! Good job.")
else:
    print("Weak password. Please make it stronger.")

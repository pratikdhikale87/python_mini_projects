import random
import string
import re

def generate_password(length=12):
    if length < 8:
        raise ValueError("Password length must be at least 8 characters")

    all_chars = string.ascii_letters + string.digits + string.punctuation

    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation),
    ]

    password += random.choices(all_chars, k=length - 4)
    random.shuffle(password)

    return "".join(password)


def validate_password(password):
    if len(password) < 8:
        return False, "At least 8 characters required"
    if not re.search(r"[A-Z]", password):
        return False, "Missing uppercase letter"
    if not re.search(r"[a-z]", password):
        return False, "Missing lowercase letter"
    if not re.search(r"\d", password):
        return False, "Missing digit"
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False, "Missing special character"

    return True, "Password is strong"


def main():
    print("1. Generate Password")
    print("2. Validate Password")

    choice = input("Choose an option (1/2): ")

    if choice == "1":
        length = int(input("Enter password length: "))
        print("Generated Password:", generate_password(length))

    elif choice == "2":
        password = input("Enter password to validate: ")
        valid, message = validate_password(password)
        print(message)

    else:
        print("Invalid choice")


if __name__ == "__main__":
    main()

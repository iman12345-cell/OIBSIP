#Iman Mirza
#Python Programming
#Task 3 - password generator


import random
import string

while True:
    print("\n===== RANDOM PASSWORD GENERATOR =====")

    # Password length
    while True:
        try:
            length = int(input("Enter password length (minimum 8): "))

            if length < 8:
                print("Password length must be at least 8.")
            else:
                break

        except ValueError:
            print("Please enter a valid number.")

    # Character type selection
    print("\nChoose character types:")
    print("1. Uppercase letters (A-Z)")
    print("2. Lowercase letters (a-z)")
    print("3. Numbers (0-9)")
    print("4. Symbols (!@#$...)")

    while True:
        choices = input(
            "Enter your choices separated by spaces (e.g. 1 2 3 4): "
        ).split()

        # Remove duplicates
        choices = list(set(choices))

        if len(choices) < 2:
            print("Please select at least 2 character types.")
            continue

        if not all(choice in ["1", "2", "3", "4"] for choice in choices):
            print("Invalid choice. Please select only 1, 2, 3, or 4.")
            continue

        break

    # Character pool
    characters = ""
    required_characters = []

    if "1" in choices:
        characters += string.ascii_uppercase
        required_characters.append(random.choice(string.ascii_uppercase))

    if "2" in choices:
        characters += string.ascii_lowercase
        required_characters.append(random.choice(string.ascii_lowercase))

    if "3" in choices:
        characters += string.digits
        required_characters.append(random.choice(string.digits))

    if "4" in choices:
        characters += string.punctuation
        required_characters.append(random.choice(string.punctuation))

    # Generate remaining characters
    remaining_length = length - len(required_characters)

    password = required_characters + [
        random.choice(characters)
        for _ in range(remaining_length)
    ]

    # Shuffle password
    random.shuffle(password)

    password = "".join(password)

    print("\nGenerated Password:", password)

    # Generate another password
    again = input("\nGenerate another password? (y/n): ").lower()

    if again != "y":
        print("Thank you for using the Password Generator!")
        break
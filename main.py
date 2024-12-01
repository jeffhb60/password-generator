import random
import string


def generate_password():
    print("Welcome to the Random Password Generator!")

    # Prompt the user for the password length
    while True:
        try:
            length = int(input("Enter the desired password length (8-256): "))
            if 8 <= length <= 256:
                break
            else:
                print("Please enter a number between 8 and 256.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Define the pool of characters
    character_pool = string.ascii_letters + string.digits + string.punctuation

    # Optionally exclude characters
    exclude_chars = input("Enter any characters you want to exclude (leave blank to include all): ")
    if exclude_chars:
        character_pool = ''.join(c for c in character_pool if c not in exclude_chars)

    if not character_pool:
        print("Error: No characters left to generate a password. Exiting.")
        return

    # Generate the password
    password = ''.join(random.choice(character_pool) for _ in range(length))

    print("\nGenerated Password:")
    print(password)


# Run the program
generate_password()

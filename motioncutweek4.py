import random
import string

def generate_password(length):
    """Generates a random password."""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    try:
        num_passwords = int(input("How many passwords would you like to generate? "))
        length = int(input("Enter the desired length for your passwords: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    if length < 8:
        print("For better security, please choose a length of at least 8 characters.")
        return

    print("\nGenerating passwords...")
    for i in range(num_passwords):
        print(f"Password {i+1}: {generate_password(length)}")

if __name__ == "__main__":
    main()

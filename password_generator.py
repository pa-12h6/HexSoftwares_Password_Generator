import random
import string


def generate_password(length, use_numbers=True, use_symbols=True):
    """Generate a strong random password."""

    if length < 4:
        raise ValueError("Password length must be at least 4 characters.")

    characters = string.ascii_letters

    if use_numbers:
        characters += string.digits

    if use_symbols:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))

    return password


def main():
    print("=" * 50)
    print("       HEXSOFTWARES PASSWORD GENERATOR")
    print("=" * 50)

    while True:
        try:
            length = int(input("\nEnter password length: "))

            if length < 4:
                print("Password length must be at least 4.")
                continue

            break

        except ValueError:
            print("Please enter a valid number.")

    numbers_choice = input("Include numbers? (y/n): ").lower()
    symbols_choice = input("Include symbols? (y/n): ").lower()

    use_numbers = numbers_choice == "y"
    use_symbols = symbols_choice == "y"

    password = generate_password(
        length,
        use_numbers,
        use_symbols
    )

    print("\nGenerated Password:")
    print("-" * 30)
    print(password)
    print("-" * 30)

    print("\nPassword generated successfully!")


if __name__ == "__main__":
    main()

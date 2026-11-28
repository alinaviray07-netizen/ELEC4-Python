
# Name: Alina E. Viray
# Section: IV-BSIT-C
# Activity: P4 - Safe Menu Program
# Date: November 20, 2026


def divide_numbers():
    try:
        first = float(input("Enter first number: "))
        second = float(input("Enter second number: "))

        result = first / second

    except ValueError:
        print("Error: Please enter valid numbers.")

    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")

    else:
        print(f"Result: {result:.2f}")

    finally:
        print("Division operation finished.")


def open_text_file():
    filename = input("Enter file name: ")

    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()

    except FileNotFoundError:
        print("Error: File not found.")

    except PermissionError:
        print("Error: You do not have permission to open this file.")

    else:
        print("\n===== FILE CONTENT =====")
        print(content)

    finally:
        print("File operation finished.")


def main():
    while True:
        print("\n===== SAFE MENU PROGRAM =====")
        print("1. Divide Two Numbers")
        print("2. Open a Text File")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            divide_numbers()

        elif choice == "2":
            open_text_file()

        elif choice == "3":
            print("Thank you for using the program!")
            break

        else:
            print("Invalid menu selection. Please try again.")


if __name__ == "__main__":
    main()

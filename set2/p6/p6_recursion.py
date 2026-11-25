
# Name: Alina E. Viray
# Section: IV-BSIT-C
# Activity: P6 - Recursion Toolkit
# Date: November 20, 2026


# Base case: n is 0 or 1.
# Recursive call: n * factorial(n - 1).
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)


# Base case: n is 0 or 1.
# Recursive call: fibonacci(n - 1) + fibonacci(n - 2).
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


# Base case: n is 0.
# Recursive call: n + sum_numbers(n - 1).
def sum_numbers(n):
    if n == 0:
        return 0
    return n + sum_numbers(n - 1)


# Base case: the list is empty.
# Recursive call: search the remaining list items.
def search(items, target):
    if not items:
        return False

    if items[0] == target:
        return True

    return search(items[1:], target)


def get_non_negative_number():
    while True:
        try:
            number = int(input("Enter a non-negative number: "))

            if number >= 0:
                return number

            print("Please enter 0 or a positive number.")

        except ValueError:
            print("Invalid input. Enter a whole number.")


def main():
    while True:
        print("\n===== RECURSION TOOLKIT =====")
        print("1. Factorial")
        print("2. Fibonacci")
        print("3. Sum of Numbers")
        print("4. Recursive Search")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            n = get_non_negative_number()
            print(f"Factorial of {n}: {factorial(n)}")

        elif choice == "2":
            n = get_non_negative_number()

            if n > 30:
                print("Please enter 30 or less for Fibonacci.")
                continue

            print(f"First {n} Fibonacci terms:")

            for i in range(n):
                print(fibonacci(i), end=" ")

            print()

            if n > 0:
                print(f"Fibonacci term at position {n}: {fibonacci(n)}")

        elif choice == "3":
            n = get_non_negative_number()
            print(f"Sum from 1 to {n}: {sum_numbers(n)}")

        elif choice == "4":
            items = input("Enter numbers separated by spaces: ")

            try:
                numbers = [int(x) for x in items.split()]
                target = int(input("Enter number to search: "))

                if search(numbers, target):
                    print("Number found in the list.")
                else:
                    print("Number not found.")

            except ValueError:
                print("Invalid input. Enter whole numbers only.")

        elif choice == "5":
            print("Thank you for using Recursion Toolkit!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

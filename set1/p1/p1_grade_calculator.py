
# Name: Alina E. Viray
# Section: IV-BSIT-C
# Activity: P1 - Student Grade Calculator
# Date: November 19, 2026


def enter_grades():
    grades = []

    while True:
        try:
            count = int(input("How many grades? "))
            if count <= 0:
                print("Please enter at least one grade.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

    for i in range(count):
        while True:
            try:
                grade = float(input(f"Enter grade {i + 1}: "))
                if 0 <= grade <= 100:
                    grades.append(grade)
                    break
                else:
                    print("Grade must be between 0 and 100.")
            except ValueError:
                print("Invalid input. Enter a number.")

    return grades


def calculate_average(grades):
    return sum(grades) / len(grades)


def get_highest(grades):
    return max(grades)


def get_lowest(grades):
    return min(grades)


def get_status(grades):
    average = calculate_average(grades)
    if average >= 75:
        return "Passed"
    return "Failed"


def display_results(grades):
    if not grades:
        print("No grades entered yet.")
        return

    print("\n===== GRADE RESULTS =====")
    print(f"Average: {calculate_average(grades):.2f}")
    print(f"Highest Grade: {get_highest(grades):.2f}")
    print(f"Lowest Grade: {get_lowest(grades):.2f}")
    print(f"Status: {get_status(grades)}")


def main():
    grades = []

    while True:
        print("\n===== STUDENT GRADE CALCULATOR =====")
        print("1. Enter Grades")
        print("2. View Results")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            grades = enter_grades()
        elif choice == "2":
            display_results(grades)
        elif choice == "3":
            print("Thank you for using the program!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()


# A local variable is declared inside a function and can only
# be accessed within that function. In this program, grades
# is a local variable inside main(). A global variable is
# declared outside functions and can be accessed by other
# functions. I used parameters instead of a global grades
# variable to keep the program organized.

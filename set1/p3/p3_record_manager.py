
# Name: Alina E. Viray
# Section: IV-BSIT-C
# Activity: P3 - Student Record Manager
# Date: November 20, 2026

# List for storing student names
students = []

# Set for checking duplicate names
student_set = set()


def add_student():
    name = input("Enter student name: ").strip()

    if not name:
        print("Student name cannot be empty.")
    elif name.lower() in student_set:
        print("Student already exists.")
    else:
        students.append(name)
        student_set.add(name.lower())
        print("Student added successfully.")


def remove_student():
    name = input("Enter student name to remove: ").strip()

    for student in students:
        if student.lower() == name.lower():
            students.remove(student)
            student_set.remove(student.lower())
            print("Student removed successfully.")
            return

    print("Student not found.")


def search_student():
    keyword = input("Enter name to search: ").strip().lower()

    if not keyword:
        print("Please enter a name to search.")
        return

    matches = [
        student for student in students
        if keyword in student.lower()
    ]

    if matches:
        print("\nSearch Results:")
        for student in sorted(matches, key=str.lower):
            print("-", student)
    else:
        print("No matching student found.")


def display_students():
    if not students:
        print("No students recorded.")
        return

    print("\n===== STUDENT LIST =====")

    for number, student in enumerate(
        sorted(students, key=str.lower), start=1
    ):
        print(f"{number}. {student}")

    print(f"Total Students: {len(students)}")


def main():
    while True:
        print("\n===== STUDENT RECORD MANAGER =====")
        print("1. Add Student")
        print("2. Remove Student")
        print("3. Search Student")
        print("4. Display All Students")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            remove_student()
        elif choice == "3":
            search_student()
        elif choice == "4":
            display_students()
        elif choice == "5":
            print("Thank you for using Student Record Manager!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()


# A list is used to store student names and allows the
# program to arrange and display them in order.
# A set only stores unique values, so I used it to check
# if a student already exists before adding a new record.
# Using both collections helps prevent duplicates while
# keeping the student names organized.

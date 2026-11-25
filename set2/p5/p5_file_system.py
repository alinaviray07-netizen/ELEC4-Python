
# Name: Alina E. Viray
# Section: IV-BSIT-C
# Activity: P5 - Student Information File System
# Date: November 20, 2026

from pathlib import Path

# Save the text file in the same folder as this program
FILE_NAME = Path(__file__).with_name("students.txt")


def load_students():
    students = []

    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            for line in file:
                data = line.strip().split("|")

                if len(data) == 4:
                    students.append(data)

    except FileNotFoundError:
        print("No existing records found. Starting a new list.")

    return students


def save_students(students):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        for student in students:
            file.write("|".join(student) + "\n")


def get_average():
    while True:
        try:
            average = float(input("Enter general average: "))

            if 0 <= average <= 100:
                return average

            print("Average must be between 0 and 100.")

        except ValueError:
            print("Invalid input. Please enter a number.")


def add_student(students):
    student_id = input("Enter student ID: ").strip()

    if not student_id:
        print("Student ID cannot be empty.")
        return

    for student in students:
        if student[0] == student_id:
            print("Student ID already exists.")
            return

    name = input("Enter full name: ").strip()
    section = input("Enter course/section: ").strip()

    if not name or not section or "|" in student_id + name + section:
        print("Invalid student information.")
        return

    average = get_average()

    students.append([
        student_id,
        name,
        section,
        str(average)
    ])

    save_students(students)
    print("Student record added successfully.")


def display_students(students):
    if not students:
        print("No student records found.")
        return

    print("\n===== STUDENT RECORDS =====")

    for student in students:
        print(f"\nStudent ID: {student[0]}")
        print(f"Full Name: {student[1]}")
        print(f"Course/Section: {student[2]}")
        print(f"General Average: {float(student[3]):.2f}")

    print(f"\nTotal Students: {len(students)}")


def search_student(students):
    student_id = input("Enter student ID to search: ").strip()

    for student in students:
        if student[0] == student_id:
            print("\nStudent Found!")
            print(f"Student ID: {student[0]}")
            print(f"Full Name: {student[1]}")
            print(f"Course/Section: {student[2]}")
            print(f"General Average: {float(student[3]):.2f}")
            return

    print("Student not found.")


def update_student(students):
    student_id = input("Enter student ID to update: ").strip()

    for student in students:
        if student[0] == student_id:
            print("\nEnter new student information.")

            name = input("New full name: ").strip()
            section = input("New course/section: ").strip()

            if not name or not section or "|" in name + section:
                print("Invalid student information.")
                return

            average = get_average()

            student[1] = name
            student[2] = section
            student[3] = str(average)

            save_students(students)
            print("Student record updated successfully.")
            return

    print("Student not found.")


def main():
    students = load_students()

    while True:
        print("\n===== STUDENT INFORMATION FILE SYSTEM =====")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Search Student by ID")
        print("4. Update Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student(students)

        elif choice == "2":
            display_students(students)

        elif choice == "3":
            search_student(students)

        elif choice == "4":
            update_student(students)

        elif choice == "5":
            print("Program closed. Student records are saved.")
            break

        else:
            print("Invalid menu selection.")


if __name__ == "__main__":
    main()

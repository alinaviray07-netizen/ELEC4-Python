
# Name: Alina E. Viray
# Section: IV-BSIT-C
# Activity: P2 - Custom Module
# Date: November 19, 2026

import student_utils
from student_utils import get_highest, get_lowest
from datetime import datetime


def main():
    grades = []

    print("===== STUDENT GRADE REPORT =====")

    while True:
        try:
            count = int(input("How many grades? "))
            if count > 0:
                break
            print("Please enter at least one grade.")
        except ValueError:
            print("Please enter a valid number.")

    for i in range(count):
        while True:
            try:
                grade = float(input(f"Enter grade {i + 1}: "))

                if 0 <= grade <= 100:
                    grades.append(grade)
                    break

                print("Grade must be between 0 and 100.")
            except ValueError:
                print("Invalid grade. Enter a number.")

    average = student_utils.calculate_average(grades)
    status = student_utils.check_status(grades)
    highest = get_highest(grades)
    lowest = get_lowest(grades)

    print("\n===== GRADE RESULTS =====")
    print(f"Average: {average:.2f}")
    print(f"Highest Grade: {highest:.2f}")
    print(f"Lowest Grade: {lowest:.2f}")
    print(f"Status: {status}")
    print("Report Generated:", datetime.now().strftime("%Y-%m-%d %I:%M %p"))


if __name__ == "__main__":
    main()

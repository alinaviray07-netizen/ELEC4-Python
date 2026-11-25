
# Name: Alina E. Viray
# Section: IV-BSIT-C
# Activity: P2 - Custom Module
# Date: November 19, 2026

# Calculate the average grade
def calculate_average(grades):
    return sum(grades) / len(grades)


# Determine if the student passed or failed
def check_status(grades):
    average = calculate_average(grades)
    return "Passed" if average >= 75 else "Failed"


# Get the highest grade
def get_highest(grades):
    return max(grades)


# Get the lowest grade
def get_lowest(grades):
    return min(grades)


# Name: Alina E. Viray
# Section: IV-BSIT-C
# Activity: P7 - Student Management System with Classes
# Date: November 20, 2026


# Class for student information
class Student:
    def __init__(self, student_id, name, grade):
        self.student_id = student_id
        self.name = name
        self.__grade = 0
        self.set_grade(grade)

    # Read the private grade
    def get_grade(self):
        return self.__grade

    # Update the grade with validation
    def set_grade(self, grade):
        if 0 <= grade <= 100:
            self.__grade = grade
            return True

        print("Invalid grade. Grade must be 0 to 100.")
        return False

    # Update student information
    def update_name(self, new_name):
        if new_name.strip():
            self.name = new_name.strip()
            print("Student name updated successfully.")
        else:
            print("Name cannot be empty.")

    # Display student information
    def display_info(self):
        print(f"ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Grade: {self.__grade}")
        print("-" * 30)


# Class for subject information
class Subject:
    def __init__(self, subject_code, subject_name):
        self.subject_code = subject_code
        self.subject_name = subject_name

    def display_subject(self):
        print(f"Subject: {self.subject_code} - {self.subject_name}")


# Class for managing students in a section
class Section:
    def __init__(self, section_name, subject):
        self.section_name = section_name
        self.subject = subject
        self.students = []

    # Add a student object
    def add_student(self, student):
        self.students.append(student)

    # Display all students in this section
    def display_students(self):
        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print(f"Section: {self.section_name}")
        self.subject.display_subject()
        print("-" * 30)

        for student in self.students:
            student.display_info()


def main():
    subject = Subject("ELEC 4", "Python Programming")

    section = Section("IV-BSIT-C", subject)

    # Create three student objects
    student1 = Student("2026-001", "Kian Cruz", 88)
    student2 = Student("2026-002", "Yuri Santos", 91)
    student3 = Student("2026-003", "Lyn Reyes", 85)

    # Add students to the section
    section.add_student(student1)
    section.add_student(student2)
    section.add_student(student3)

    # Update one student's information
    print("===== UPDATING STUDENT =====")
    student1.update_name("Kian D. Cruz")
    student1.set_grade(93)

    # Test invalid grade
    print("\n===== GRADE VALIDATION =====")
    student2.set_grade(105)

    # Display all students
    section.display_students()


if __name__ == "__main__":
    main()


# Name: Alina E. Viray
# Section: IV-BSIT-C
# Activity: P8 - Inheritance and Polymorphism
# Date: November 20, 2026


# Parent class with common information
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"My name is {self.name} and I am {self.age} years old.")


# Student inherits from Person
class Student(Person):
    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course

    # Override the parent method
    def introduce(self):
        print(f"I am {self.name}, {self.age} years old, "
              f"and I am studying {self.course}.")


# Teacher also inherits from Person
class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    # Override the parent method
    def introduce(self):
        print(f"I am {self.name}, {self.age} years old, "
              f"and I teach {self.subject}.")


def main():
    # Create objects from different classes
    person = Person("Alex Reyes", 30)
    student1 = Student("Kian Cruz", 21, "BSIT")
    student2 = Student("Yuri Santos", 22, "BSIT")
    teacher = Teacher("Ms. Lyn Reyes", 35, "Python Programming")

    # Polymorphism using a list of different objects
    people = [person, student1, student2, teacher]

    print("===== INHERITANCE AND POLYMORPHISM =====")

    for individual in people:
        individual.introduce()


if __name__ == "__main__":
    main()


# Inheritance allows the Student and Teacher classes to
# reuse the attributes and methods of the Person class.
# I used super().__init__() to initialize the common
# information from the parent class. Polymorphism is shown
# when different objects are placed in one list and the
# same introduce() method produces different outputs.

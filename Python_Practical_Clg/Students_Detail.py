# Student Details Using Class and Object

class Student:
    def __init__(self, name, roll_no, course):
        self.name = name
        self.roll_no = roll_no
        self.course = course

    def display_details(self):
        print("Student Name:", self.name)
        print("Roll Number:", self.roll_no)
        print("Course:", self.course)


# Creating an object
s1 = Student("Anshu", 12, "B.Sc. Computer Science (Hons.)")

# Displaying student details
s1.display_details()


OUTPUT
Student Name: Anshu
Roll Number: 12
Course: B.Sc. Computer Science (Hons.)

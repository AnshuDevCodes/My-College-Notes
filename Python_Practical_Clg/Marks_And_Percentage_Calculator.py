# Student Marks and Percentage Calculator

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def calculate_total(self):
        return sum(self.marks)

    def calculate_percentage(self):
        return self.calculate_total() / len(self.marks)

    def display(self):
        print("Student Name:", self.name)
        print("Marks:", self.marks)
        print("Total Marks:", self.calculate_total())
        print("Percentage:", self.calculate_percentage(), "%")


# Creating an object
s1 = Student("Anshu", [85, 90, 88, 92, 80])

s1.display()


OUTPUT
Student Name: Anshu
Marks: [85, 90, 88, 92, 80]
Total Marks: 435
Percentage: 87.0 %

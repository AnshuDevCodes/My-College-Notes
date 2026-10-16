# Employee Management System

class Employee:
    def __init__(self, name, employee_id, monthly_salary):
        self.name = name
        self.employee_id = employee_id
        self.monthly_salary = monthly_salary

    def calculate_annual_salary(self):
        return self.monthly_salary * 12

    def display_details(self):
        print("Employee Name:", self.name)
        print("Employee ID:", self.employee_id)
        print("Monthly Salary:", self.monthly_salary)
        print("Annual Salary:", self.calculate_annual_salary())


# Creating an object
e1 = Employee("Rahul", 101, 25000)

# Displaying employee details
e1.display_details()


OUTPUT
Employee Name: Rahul
Employee ID: 101
Monthly Salary: 25000
Annual Salary: 300000

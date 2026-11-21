class Employee:

    count = 0

    def __init__(self, emp_no, name, dept, basic, da, hra):
        if basic < 0 or da < 0 or hra < 0:
            raise ValueError("Salary components cannot be negative")

        self.emp_no = emp_no
        self.name = name
        self.dept = dept
        self.basic = basic
        self.da = da
        self.hra = hra

        Employee.count += 1

    # Calculate total salary
    def salary(self):
        return self.basic + self.da + self.hra

    # Display employee details
    def __str__(self):
        return (
            f"Employee Number: {self.emp_no}\n"
            f"Name: {self.name}\n"
            f"Department: {self.dept}\n"
            f"Basic: {self.basic}\n"
            f"DA: {self.da}\n"
            f"HRA: {self.hra}\n"
            f"Total Salary: {self.salary()}"
        )

    # Decrease object count
    def __del__(self):
        Employee.count -= 1


# Create employee object
e1 = Employee(101, "Anshu", "Computer Science", 20000, 5000, 3000)

print(e1)

print("Total Employees:", Employee.count)

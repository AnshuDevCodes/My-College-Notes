# Electricity Bill Calculator

class ElectricityBill:
    def __init__(self, name, units):
        self.name = name
        self.units = units

    def calculate_bill(self):
        if self.units <= 100:
            bill = self.units * 3
        elif self.units <= 200:
            bill = (100 * 3) + (self.units - 100) * 5
        else:
            bill = (100 * 3) + (100 * 5) + (self.units - 200) * 7

        return bill

    def display(self):
        print("Customer Name:", self.name)
        print("Units Consumed:", self.units)
        print("Electricity Bill: Rs.", self.calculate_bill())


# Creating an object
customer = ElectricityBill("Anshu", 250)

customer.display()


OUTPUT
Customer Name: Anshu
Units Consumed: 250
Electricity Bill: Rs. 1050

# Online Shopping System

class Shopping:
    def __init__(self, product_name, price, quantity):
        self.product_name = product_name
        self.price = price
        self.quantity = quantity

    def calculate_total(self):
        return self.price * self.quantity

    def display_bill(self):
        print("Product Name:", self.product_name)
        print("Price per Item: Rs.", self.price)
        print("Quantity:", self.quantity)
        print("Total Amount: Rs.", self.calculate_total())


# Creating an object
item = Shopping("Notebook", 50, 4)

# Displaying the bill
item.display_bill()



OUTPUT
Product Name: Notebook
Price per Item: Rs. 50
Quantity: 4
Total Amount: Rs. 200

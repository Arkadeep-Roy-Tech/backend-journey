# SECTION D — Write Code Cold (2 problems, 20 marks each = 40 marks)
# Full solutions, your own naming.
# D1 — (20 marks)

# Write a function that takes a list of numbers and returns the largest one — without using Python's built-in max(). Then call it on a list and print the result.
# D2 — (20 marks) — StockSense flavor

# Write a class representing a product in inventory. It should store a name, a price, and a quantity when created. Give it:

# a method that returns the total value of that product's stock (price × quantity)
# a method that takes an amount and reduces the quantity by that amount, but only if there's enough stock — otherwise it returns a message saying there isn't enough.

# Create a product, sell some stock, print the result, and print the total value afterward.

numbers = [20, 15, 12, 2, 100, 7, 35]

def largest_one(numbers):
    largest_number = numbers[0]
    for number in numbers:
        if number > largest_number:
            largest_number = number
    return largest_number

result = largest_one(numbers)
print(f"The largest number in the list is : {result}")

# D2 — (20 marks) — StockSense flavor

# Write a class representing a product in inventory. It should store a name, a price, and a quantity when created. Give it:

# a method that returns the total value of that product's stock (price × quantity)
# a method that takes an amount and reduces the quantity by that amount, but only if there's enough stock — otherwise it returns a message saying there isn't enough.

# Create a product, sell some stock, print the result, and print the total value afterward.

class ProductInventory:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def total_stock_value(self):
        return self.price * self.quantity
    
    def stock_amount(self, amount):
        if self.quantity < amount:
            return "There isn't enough stock in inventory."
        return self.quantity - amount

inventory_tool = ProductInventory("Mobile", 6000, 30)
result_of_stock_value = inventory_tool.total_stock_value()
result_stock_amount = inventory_tool.stock_amount(50)

print(f"Total stock is worth : {result_of_stock_value:,.2f} rupees.")
print(f"Current stock after deduction is : {result_stock_amount} pieces.")
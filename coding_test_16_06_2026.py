# 💻 CODING TEST — Phase 1 + 1.5 (Coding Only)
# Cold. No notes, no Google. You name everything. Ramps in difficulty.
# Problem 1 — warm-up 🟢

# You're given a list of words. Return a new list containing only the words longer than 4 characters, with each of those words in uppercase. (Think: which two tools combine here.)

# words = ["Apple","TV","Music","Pineapple","Vegetable","Pie"]
# new_list = [word.upper() for word in words if len(word) > 4]
# print(new_list)

# Problem 2 — combine concepts 🟡

# Write a function that takes a list of numbers and returns a dictionary with two things: how many numbers were even, and how many were odd. 
# The caller should be able to read both counts back out.

# numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13]

# def odd_even(numbers):
#     even = []
#     odd = []
#     for number in numbers:
#         if number % 2 == 0:
#             even.append(number)
#         else:
#             odd.append(number)
#     return {"even count": len(even), "odd count": len(odd)}

# result = odd_even(numbers)
# print(result)

# Problem 3 — the curveball 🟠

# You're given a list of dictionaries, where each represents a sale with a product name and an amount. 
# Write a function that returns the name of the product with the highest total amount across all its sales — note a product can appear more than once in the list, so you must add up each product's sales before deciding the winner. 
# Return the single top product's name.
# Example input meaning: if "Mouse" appears twice (200 and 300) and "TV" once (400), Mouse totals 500 and wins over TV's 400.

# sale = [
#     {"name": "TV", "amount": 25000},
#     {"name": "Mobile", "amount": 5000},
#     {"name": "Mobile", "amount": 22000},
#     {"name": "Laptop", "amount": 45000},
#     {"name": "Watch", "amount": 10000}
# ]

# def highest_sale(sale):
#     item_total_sale = {}

#     for item in sale:
#         product_name = item["name"]
#         amount = item["amount"]
#         if product_name in item_total_sale:
#             item_total_sale[product_name] += amount
#         else:
#             item_total_sale[product_name] = amount
#     highest_total = 0
#     top_product = None
#     for product, total_amount in item_total_sale.items():
#         if total_amount > highest_total:
#             highest_total = total_amount
#             top_product = product
#     return top_product

# result = highest_sale(sale)
# print(result)

# Problem 4 — the hard one (stretch above interview level) 🔴

# Write a class representing a simple inventory. It starts empty. It should let you:

# add a product with a name, price, and quantity (if the product already exists, increase its quantity instead of duplicating it)
# remove a quantity of a product (if removing more than exists, or the product doesn't exist, handle it gracefully — don't crash)
# return the total value of the entire inventory (sum of price × quantity across all products)
# return the name of the single most valuable product line (price × quantity)

# Create the inventory, do a few operations, and print results that prove each method works — including at least one operation that should fail gracefully.

class Inventory:
    def __init__(self):
        self.products = {}
    
    def add_product(self, name, price, quantity):
        if name in self.products:
            self.products[name]["quantity"] += quantity
        else:
            self.products[name] = {"price": price, "quantity": quantity}
    
    def remove_product(self, name, amount):
        if name in self.products:
            if self.products[name]["quantity"] < amount:
                return "Cannot remove as amount to remove is more than present qantity."
            else:
                self.products[name]["quantity"] -= amount
                return "Product quantity removed."
        else:
            return "Product doesn't exist."
    
    def total_value(self):
        total = 0
        for product in self.products.values():
            total += product["price"] * product["quantity"]
        return total

    def most_valuable_product(self):
        highest_total = 0
        top_product_name = None
        for name, details in self.products.items():
            if highest_total < details["price"] * details["quantity"]:
                highest_total = details["price"] * details["quantity"]
                top_product_name = name
        return top_product_name

        

invi = Inventory()
invi.add_product("Mobile", 8000, 5)
invi.add_product("Mobile", 8000, 10)
invi.add_product("TV", 15000, 1)
result_total_value = invi.total_value()
result_most_val_pdt = invi.most_valuable_product()
print(invi.products)
print(result_total_value)
print(result_most_val_pdt)
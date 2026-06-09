'''Problem 1 — Look It Up 🟢
You've got a single product dictionary:
pythonproduct = {"name": "Mouse", "price": 499, "quantity": 30}
Ask the user (or just hardcode a variable) for a field name like "price", and print its value safely — so that if someone asks for a field that doesn't exist (like "color"), your code prints "Field not found" instead of crashing.
Think: which dictionary tool returns None instead of crashing? And how do you check if what came back was None?'''

product = {"name": "Mouse", "price": 499, "quantity": 30}

user_input = input("Please enter a field name that you wish to look up: ")
value = product.get(user_input)

if value is None:
    print("Field not found")
else:
    print(f"{user_input} of the item is {value}")

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

'''Problem 2 — Total Inventory Value 🟡 (StockSense flavour)
Here's a small inventory — a list of dictionaries:
pythoninventory = [
    {"name": "Mouse", "price": 499, "quantity": 30},
    {"name": "Keyboard", "price": 899, "quantity": 15},
    {"name": "TV", "price": 25000, "quantity": 4}
]
Loop through it and calculate the total value of all stock — that's each product's price × quantity, all summed together. Print the final total.
Think: one running total before the loop, and inside the loop you pull two values from each dictionary and multiply them.'''

inventory = [
    {"name": "Mouse", "price": 499, "quantity": 30},
    {"name": "Keyboard", "price": 899, "quantity": 15},
    {"name": "TV", "price": 25000, "quantity": 4}
]

total_worth_of_stocks = 0

for product in inventory:
    total_value_of_each_item = product["price"] * product["quantity"]
    total_worth_of_stocks += total_value_of_each_item
print(f"Total value of the inventory is = ${total_worth_of_stocks}")

#------------------------------------------------------------------------------------------------------------------------------------------------

'''Problem 3 — Find the Expensive Ones 🔴
Same inventory as Problem 2. Loop through and print the name of every product that costs more than ₹500. Skip the rest.
Keyboard
TV
Think: loop the list, pull each product's price, an if to test the threshold, print the name only when it passes.'''

inventory = [
    {"name": "Mouse", "price": 499, "quantity": 30},
    {"name": "Keyboard", "price": 899, "quantity": 15},
    {"name": "TV", "price": 25000, "quantity": 4}
]

for product in inventory:
    if product["price"] > 500:
        print(product["name"])
def greet():
    print("Hello from the other side!")

greet()

def greet2(first, last):
    print(f"The names {last}, {first} {last}.")

greet2("James","Bond")

def add_print(a, b):
    print(a + b)

def add_return(a, b):
    return a + b 

x = add_print(3, 5)
y = add_return(3, 5)

print(x)
print(y)


inventory = [
    {"name": "Mouse", "price": 499, "quantity": 30},
    {"name": "Keyboard", "price": 899, "quantity": 15},
    {"name": "TV", "price": 25000, "quantity": 4}
]

def calculate_total(inventory):
    total_stock_value = 0
    for product in inventory:
        product_total_value = product["price"] * product["quantity"]
        total_stock_value += product_total_value
    return total_stock_value

result = calculate_total(inventory)
print(result)
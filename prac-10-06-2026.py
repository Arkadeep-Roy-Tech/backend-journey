'''product_a = {"name": "Mouse", "quantity": 30}
product_b = {"name": "Webcam", "quantity": 0}

def is_in_stock(product):
    return product["quantity"] > 0

result = is_in_stock(product_a)
print(result)'''

#-----------------------------------------------------------------------------------------------------

'''def apply_discount(price, percent):
    return round(price - (percent / 100 * price), 2)

result = apply_discount(798, 20)
print(f"Discounted price is : {result}")'''

#-----------------------------------------------------------------------------------------------------

inventory = [
    {"name": "Mouse", "quantity": 30},
    {"name": "Keyboard", "quantity": 3},
    {"name": "TV", "quantity": 0},
    {"name": "Cable", "quantity": 50}
]

def count_low_stock(inventory, threshold):
    count = 0
    for product in inventory:
        if product["quantity"] < threshold:
            count += 1
    return count

result = count_low_stock(inventory, 5)
print(result)
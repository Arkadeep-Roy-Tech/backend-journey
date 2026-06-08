product = {
    "name" : "Mouse",
    "price" : 499,
    "quantity" : 25 
}

print(product["quantity"])
product["quantity"] = 30
product["brand"] = "Logitech"

print(product)

#print(product["color"]) To test error.
#print(product)

print(product.get("price"))
print(product.get("color"))

product.pop("brand")
print(product)

for key, value in product.items():
    print(f"{key}: {value}")

inventory = [
    {"name": "Mouse", "price": 999},
    {"name": "Keyboard", "price": 899},
    {"name": "TV", "price": 25000}
]

for inventory_items in inventory:
    print(f"{inventory_items.get("name")} costs {inventory_items.get("price")}")
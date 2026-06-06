products = ["Mouse", "Keyboard", "TV"]

for index, product in enumerate(products):
    print(f"{index+1}. {product}")

print(products[0])
print(products[2])
print(products[3])

products[1] = "Webcam"
products.append("Monitor")
print(products)

products.pop(3)
print(products)
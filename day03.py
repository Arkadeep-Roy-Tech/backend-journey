item_total_stock = 200
item_sales = 2

if item_total_stock > 100 and item_sales < 10:
    print("Apply heavy discount.")
elif item_total_stock > 100 or item_sales < 10:
    print("Apply mild discount.")
else:
    print("No discount needed.")


product_name = input("Enter a product name: ")
stock_count = int(input("Enter the stock count: "))

if stock_count > 100:
    print(product_name + " has high stock.")
else:
    print(product_name + " has low stock.")
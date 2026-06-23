# name = "  inventory   "
# clean_name = name.strip()
# print(clean_name)

# raw_colors = "red|green|blue"
# colors = raw_colors.split("|")
# print(colors)

# year_month_day = ["2026","06","22"]
# formatted_date = "-".join(year_month_day)

# print(formatted_date)

# Problem 1.

# Write a small function that takes a price and returns that price with 18% tax added. 
# There's a tax rate value defined once at the top of your file. The function should read that rate to do its calculation — not have the number hardcoded inside it, and not reassign it. 
# Call the function with a price and print the result. (You name everything; you pick the price.)

# tax_rate = 0.18

# def taxed_price(price):
#     new_price_after_tax = price + (price * tax_rate)
#     return new_price_after_tax

# result = taxed_price(100)
# print(result)

#Problem 2.

# total = 100
# def add_bonus():
#     global total
#     total = total + 50
#     return total

# print(add_bonus())

default_status = "unknown"
def formatted_inventory_record(inventory_record):
    fields = inventory_record.split("|")
    clean_fields = []
    for item in fields:
        clean_fields.append(item.strip())
    product_name = clean_fields[0].lower()
    quantity = clean_fields[1]
    status = clean_fields[2]
    if not status:
        status = default_status
    return product_name, quantity, status

product_name, quantity, status_check = formatted_inventory_record("  Widget-A | 50 |   ")
print(f"{product_name}\n{quantity}\n{status_check}")
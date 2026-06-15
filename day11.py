# numbers = [1,2,3,4,5,6]
# evens = [n for n in numbers if n % 2 == 0]
# print(evens)

# numbers = [1,2,3,4,5,6]
# doubled = [n * 2 for n in numbers]
# evens = [n for n in numbers if n % 2 == 0]
# print(doubled)
# print(evens)

# total = 1000000
# print(f"{total:,}")

# price = 463.9999
# print(f"{price:.2f}")

# prices = [100, 250, 999, 1500]
# new_prices_with_tax = [price + (price * 0.10) for price in prices]
# print(new_prices_with_tax)

quantities = [30, 3, 50, 8, 0]
low_stock_quantitites = [quantity for quantity in quantities if quantity < 10]
count = len(low_stock_quantitites)
print(f"The total number of items that are low on stock are : {count}")
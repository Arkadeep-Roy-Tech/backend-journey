# def average_of_numbers(*args):
#     total = 0
#     for number in args:
#         total += number
#     average = total / len(args)
#     return average

# two_number_avg = average_of_numbers(9,1)
# three_number_avg = average_of_numbers(2,4,6)
# print(two_number_avg)
# print(three_number_avg)

# def product_details(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key} -> {value}")

# product_details(name="Apple", price=400, category="Fruit", stock=True)
# product_details(name="Kiwi", price=300)


# Problem 1

# def total_price_and_count(*args):
#     return sum(args), len(args)

# first_total, first_count = total_price_and_count(1,2,3)
# second_total, second_count = total_price_and_count(1,2)
# print(f"Total price for example 1 = {first_total}\nTotal count for example 1 = {first_count}")
# print(f"Total price for example 2 = {second_total}\nTotal count for example 2 = {second_count}")

# Problem 2 

def print_product_details(category, **kwargs):
    print(f"Category -> {category}")
    for key, value in kwargs.items():
        print(f"{key} -> {value}")

print_product_details("Fruit", name="Apple", color="Red")
print_product_details("Fruit", name="Kiwi", color="Green", size="small", quantity=30)
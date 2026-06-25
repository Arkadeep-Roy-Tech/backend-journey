# sqr_number = lambda number: number ** 2
# result = sqr_number(5)
# print(result)

# item_detail = [{"name": "TV", "price": 29000}, {"name": "Mobile", "price": 3300}, {"name": "Laptop", "price": 21000}]
# result = sorted(item_detail, key = lambda detail: detail["price"], reverse = True)
# print(result)


# Problem 1

# product_details = [{"name": "TV", "price": 25000, "stock": 25}, {"name": "Laptop", "price": 45000, "stock": 15}, {"name": "Mobile", "price": 9000, "stock": 35}]
# sorted_details = sorted(product_details, key = lambda detail: detail["stock"])
# print(sorted_details)

# Problem 2

person_details = [{"name": "Arka", "age": 22}, {"name": "Shruti", "age": 22}, {"name": "Dhriti", "age": 19}]
sorted_person_details = sorted(person_details, key = lambda detail: (detail["age"], detail["name"]))
print(sorted_person_details)
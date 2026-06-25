# Problem 1

# product_codes = "MK01,                 KK21,  sK11     , mk01,  fg11,      Er45    , fG11"
# def clean_product_codes(codes):
#     codes_split = codes.split(",")
#     clean_codes = set(code.strip().lower() for code in codes_split)
#     code_count = len(clean_codes)
#     return clean_codes, code_count

# clean_codes, code_count = clean_product_codes(product_codes)
# print(f"{clean_codes}\nTotal code count = {code_count}")


# Problem 2

# def average_of_scores(*args):
#     if not args:
#         raise ValueError("Nothing to average.")
#     average = sum(args) / len(args)
#     return average

# try:
#     result = average_of_scores(5,3)
#     print(result)
# except ValueError as e:
#     print(f"Invalid: {e}")

# try:
#     result = average_of_scores()
#     print(result)
# except ValueError as e:
#     print(f"Invalid: {e}")


# Problem 3

# employee_details = [{"name": "Arka", "department": "HR", "salary": 27000}, {"name": "Roy", "department": "IT", "salary": 33000}, {"name": "Shruti", "department": "Support", "salary": 31000}, {"name": "Dhriti", "department": "IT", "salary": 31000}]
# def sorted_employee_data(datalist):
#     return sorted(datalist, key = lambda data: (data["department"], -data["salary"]))

# result = sorted_employee_data(employee_details)
# print(result)


# Problem 4

def user_registration(username, **kwargs):
    if not username:
        raise ValueError("Username cannot be empty.")
    if "age" in kwargs:
        if kwargs["age"] < 0 or kwargs["age"] > 130:
            raise ValueError("Age cannot be less than 0 or more than 130.")
    print(f"Username is : {username}\nExtra profile fields provided are : {len(kwargs)}")

try:
    user_registration("", age = 22, dep = "IT")
except ValueError as e:
    print(f"Incorrect: {e}")
finally:
    print("registration attempt finished.")

try:
    user_registration("Arka", age = 22, dep = "IT")
except ValueError as e:
    print(f"Incorrect: {e}")
finally:
    print("registration attempt finished.")

try:
    user_registration("Arka", age = 222, dep = "IT")
except ValueError as e:
    print(f"Incorrect: {e}")
finally:
    print("registration attempt finished.")
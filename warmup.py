# numbers = [2, 4, 1, 5]

# def running_total(numbers):
#     total = 0
#     new_running_total = []
#     for num in numbers:
#         total += num
#         new_running_total.append(total)
#     return new_running_total

# result = running_total(numbers)
# print(result)

# list_of_strings = ["10", "hello", "20", "xyz", "30"]
# # list_of_strings = ["hello", "xyz"]

# def check_valid(list_of_strings):
#     valid_list = []
#     total = 0
#     avg = 0
#     for item in list_of_strings:
#         try:
#             valid_list.append(int(item))
#         except ValueError:
#             continue
#     if len(valid_list) != 0:
#         total = sum(valid_list)
#         avg = total / len(valid_list)
#         return round(avg,2)
#     else:
#         return "No valid numbers to perform average."

# result_check_valid = check_valid(list_of_strings)
# print(result_check_valid)


# The problem:
# You're given a list of integers that's supposed to contain every number from 1 to N exactly once — but exactly one number is missing, and one number appears twice instead. Write a function that returns both the missing number and the duplicated number.
# Example: given [1, 2, 2, 4, 5] — this should contain 1 through 5, but 3 is missing and 2 appears twice. 
# So you'd return both: duplicate is 2, missing is 3.
# Another: [1, 3, 3] → should be 1 to 3; duplicate is 3, missing is 2.
# The list won't be sorted, and N is just however long the list is.

example_list = [1, 2, 2, 4, 5]

def dup_and_miss(example_list):
    temp_list = []

    index_list = list(range(1, len(example_list) + 1))
    result_set = set(index_list) - set(example_list)
    missing_number = list(result_set)[0]

    for item in example_list:
        if item in temp_list:
            duplicate_number = item
        else:
            temp_list.append(item)
    return missing_number, duplicate_number

miss, dup = dup_and_miss(example_list)
print(f"Missing number is {miss} and duplicate number is {dup}.")
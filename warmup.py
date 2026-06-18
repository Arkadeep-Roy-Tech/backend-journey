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

list_of_strings = ["10", "hello", "20", "xyz", "30"]
# list_of_strings = ["hello", "xyz"]

def check_valid(list_of_strings):
    valid_list = []
    total = 0
    avg = 0
    for item in list_of_strings:
        try:
            valid_list.append(int(item))
        except ValueError:
            continue
    if len(valid_list) != 0:
        total = sum(valid_list)
        avg = total / len(valid_list)
        return round(avg,2)
    else:
        return "No valid numbers to perform average."

result_check_valid = check_valid(list_of_strings)
print(result_check_valid)
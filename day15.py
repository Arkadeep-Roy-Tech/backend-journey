# def divide(number1, number2):
#     try:
#         division_result = number1 / number2
#         print(division_result)
#     except ZeroDivisionError:
#         print("Cannot divide by zero.")
#     finally:
#         print("Division attempt completed.")

# divide(10, 2)
# divide(10, 0)

# def check_age(age):
#     if age < 0 or age > 130:
#         raise ValueError("Age cannot be negative or above 130.")
#     print("It's a valid age.") # only reached if the raise didn't fire

# try:
#     check_age(139)
# except ValueError as e:
#     print(f"Rejected : {e}")

# try:
#     check_age(129)
# except ValueError as e:
#     print(f"Rejected : {e}")

# def username_check(username):
#     if not username:
#         raise ValueError("Username cannot be empty.")
#     print("Valid username.")

# try:
#     username_check("")
# except ValueError as e:
#     print(f"Rejected: {e}")

# Problem 1

# def bank_withdrawal_feature(current_balance, withdrawl_amount):
#     if withdrawl_amount < 0:
#         raise ValueError("Cannot withdraw negative amount.")
#     elif withdrawl_amount > current_balance:
#         raise ValueError("Insufficient funds in your account.")
#     updated_balance = current_balance - withdrawl_amount
#     print(updated_balance)
    

# try:
#     bank_withdrawal_feature(1000, 500)
# except ValueError as e:
#     print(f"Rejected : {e}")
# finally:
#     print("Transaction completed.")

# try:
#     bank_withdrawal_feature(1000, -500)
# except ValueError as e:
#     print(f"Rejected : {e}")
# finally:
#     print("Transaction completed.")

# try:
#     bank_withdrawal_feature(1000, 2000)
# except ValueError as e:
#     print(f"Rejected : {e}")
# finally:
#     print("Transaction completed.")


# Problem 2

def mystery(x):
    try:
        if x < 0:
            raise ValueError("negative")
        return "try-block"
    except ValueError:
        return "except-block"
    finally:
        print("finally-block")

print(mystery(5))
print(mystery(-1))
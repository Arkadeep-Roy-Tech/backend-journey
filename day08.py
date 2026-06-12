#try:
#    number = int("Hello")
#    print(number)
#except:
#    print("Not a valid number.")
#print("Still running.")

def testing_error_with_try_and_except():
    while True:
        try:
            number = int(input("Enter a number: "))
            return number
        except ValueError:
            print("The input is not a valid number.Try again")

result = testing_error_with_try_and_except()
print(result)
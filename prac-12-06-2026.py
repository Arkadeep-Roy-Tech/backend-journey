#Problem 1 — Safe Divide 🟢

#Write a function safe_divide(a, b) that returns a / b, but if b is 0 (which crashes with ZeroDivisionError), catch it and return the string "Cannot divide by zero".
#Test: safe_divide(10, 2) → 5.0, and safe_divide(10, 0) → "Cannot divide by zero".
#New error type for you: dividing by zero throws ZeroDivisionError.

def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Cannot divide by zero.")
        return 0.0

result = safe_divide(10, 0)
print(result)

#Problem 2 — Safe Lookup 🟡

#Write a function get_quantity(product) that takes a product dict and returns its "quantity". If the key doesn't exist, catch the KeyError and return 0 instead.
#pythongood = {"name": "Mouse", "quantity": 30}
#bad = {"name": "Webcam"}
#get_quantity(good) → 30, get_quantity(bad) → 0.

#(Yes, .get() could also do this — but here practice the try/except way on purpose.)

good = {"name": "Mouse", "quantity": 30}
bad = {"name": "Webcam"}

def get_quantity(product):
    try:
        return product["quantity"]
    except KeyError:
        return 0

result = get_quantity(bad)
print(result)

#Problem 3 — Safe Number Parser 🔴

#Write a function parse_total(values) that takes a list of strings, tries to convert each to an integer and add it to a running total, but skips any string that isn't a valid number (catch the ValueError and continue). Return the total.
#pythondata = ["10", "abc", "5", "xyz", "20"]
#parse_total(data) → 35 (10 + 5 + 20, skipping the junk).

#This one combines a loop + try/except — the real "clean the messy data feed" pattern.

data = ["10", "abc", "5", "xyz", "20"]

def parse_total(values):
    total = 0
    for item in values:
        try:
            total += int(item)
        except ValueError:
            continue
    return total

result = parse_total(data)
print(result)
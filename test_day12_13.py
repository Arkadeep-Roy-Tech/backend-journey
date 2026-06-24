# COLD MINI-TEST — Days 12–13 (coding-first)
# Problem 1 — warmup, but combines two topics.

# A raw string comes in holding several tags separated by commas, with messy casing and stray spaces around each, like one continuous blob a user typed. Some tags are accidentally repeated. Produce a collection of the cleaned-up tags with no duplicates and no stray spacing, all in consistent casing. Print it.

# raw_string = " Darklord12,  opa29, KEIID21, seAi9,     poek12, saa21                    , sAA21, OPa29"
# raw_tags = raw_string.split(",")
# clean_tags = set(tag.strip().lower() for tag in raw_tags)

# print(clean_tags)


# Problem 2 — scope + return discipline.

# Write a function that takes a single price and returns that price with a service charge added. The service-charge rate lives as one value at the top of your file. 
# The function must use that rate without reassigning it, and must hand the result back (not print it). Then call it and print the result outside the function.

# service_charge = 0.18

# def updated_price(price, charge):
#     return price + (price * charge)

# result = updated_price(100, service_charge)
# print(result)


# Problem 3 — the curveball. This one's the stretch; expect to struggle.

# You're given two separate raw strings. Each holds a list of usernames separated by commas, with inconsistent casing and spacing throughout. 
# Find the usernames that appear in both strings — cleaned, deduplicated, case-consistent — and return them from a function as a single collection. 
# The function should take the two raw strings as inputs and not depend on anything outside itself. 
# Call it and print the shared usernames.

raw_string_1 = "Arka,   arka,  Roy, shRuti,   LiLy,            jOSe, kean "
raw_string_2 = "            arka              , lilY, JOSE"

def clean_strings(string1, string2):
    string1_split = string1.lower().split(",")
    string2_split = string2.lower().split(",")

    clean_username_set1 = set(name.strip() for name in string1_split)
    clean_username_set2 = set(name.strip() for name in string2_split)

    common_names = clean_username_set1.intersection(clean_username_set2)
    return common_names

result = clean_strings(raw_string_1, raw_string_2)
print(f"Common usernames are {result}.")
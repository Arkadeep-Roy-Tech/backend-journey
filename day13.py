# lat_long = (18.4902, 114.6291)
# print(lat_long[0])
# lat_long[0] = 12.8739

# signup_email_list = ["asdfg@hj.com", "Asdfg@hj.com", "iop@hj.com", "qwe@hj.com"]
# clean_signup_email_list = [email.lower() for email in signup_email_list ]
# unique_signup_email_list = set(clean_signup_email_list)
# print(unique_signup_email_list)

# def membership_test(signup_email, clean_emails):
#     return signup_email in clean_emails

# result = membership_test("iop@hj.com", unique_signup_email_list)
# print(result)

# Problem 1 (straightforward).

# You have two separate lists: the usernames who completed level 1 of a game, and the usernames who completed level 
# 2. Some people are in both, some in only one. Find the usernames who completed both levels. 
# (Hint: sets have a built-in way to find what two sets share — it's called intersection. 
# You haven't seen the syntax. Look it up, that's a real skill, then use it. I'll review what you find.)

# level1_completed_users = ["Arka","Roy","Sean","Kean","Shruti"]
# level2_completed_users = ["Shruti","Arka","kean"]

# level1_clean_list = [name.lower() for name in level1_completed_users]
# level2_clean_list = [name.lower() for name in level2_completed_users]

# level1_set = set(level1_clean_list)
# level2_set = set(level2_clean_list)

# users_completed_both_levels = level1_set.intersection(level2_set)
# print(users_completed_both_levels)


# Problem 2 — the curveball.

# You're given a single list of words, and some words repeat.
# Without using any if statements to check for duplicates manually, produce a report showing how many unique words there are, and how many total words there were originally.
# Then answer in a comment: if the unique count equals the total count, what does that tell you about the original list?

example_list = ["apple", "kiwi", "Mango", "KIwi", "pineapple", "maNgo", "dragonfruit"]
clean_example_list = [word.lower() for word in example_list]

unique_words = set(clean_example_list)
unique_count = len(clean_set)
total_count = len(clean_example_list)

print(f"Total unique words are : {total_items_in_set} and total words in original list : {total_items_in_original_list}")
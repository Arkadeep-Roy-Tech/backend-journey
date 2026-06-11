'''
1. Palindrome Number — LeetCode #9 🟢
Given an integer, return True if it reads the same forwards and backwards. Determine whether an integer is a palindrome. Tools: conditionals, type conversion, string/list reversal. Pure Day 1–5 stuff. Best warm-up.
'''

'''def palindrome_check(number):
    normal_number_str = str(number)
    reverse_number_str = normal_number_str[::-1]
    return normal_number_str == reverse_number_str
        
result = palindrome_check(121)
print(result)'''

'''2. Two Sum — LeetCode #1 🟡
Given a list of numbers and a target, return the positions of the two numbers that add up to the target. 
This is the classic first problem, and it's perfect for you because it covers key concepts such as iterating over lists and using dictionaries for efficient lookup. 
You can solve it with a loop + dictionary — exactly your Day 5–6 skills. Genuinely the best single problem to test everything you've learned this week. 
'''

nums = [2, 7, 11, 15]
target = 9

def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

result = two_sum(nums, target)
print(result)
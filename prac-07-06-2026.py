#Problem 1 — FizzBuzz Lite 🟢
#Loop through numbers 1 to 20. For each number:

#if it's divisible by 3, print "Fizz" instead of the number
#otherwise, just print the number

#1
#2
#Fizz
#4
#5
#Fizz
#...
#Hint you're allowed: the leftover after division is the % operator (modulo). 6 % 3 is 0. You met % on Day 2. That's your "is it divisible" test.

for number in range(1, 21):
    if number % 3 == 0:
        print("Fizz")
    else:
        print(number)

#-------------------------------------------------------------------------------------------------------------------------------------------------


#Problem 2 — Find the Max 🟡
#Given this list, find and print the largest number — without using Python's built-in max(). You have to loop and figure it out yourself.
#numbers = [4, 11, 7, 23, 9, 2, 18]
#Think: how would a human do it? You'd keep track of "biggest seen so far" and update it whenever you find something bigger. That's a variable + a loop + an if. You have all three.

numbers = [4, 11, 7, 23, 9, 2, 18]
largest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

print(largest)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Problem 3 — Count the Valid Stock 🔴 (StockSense flavour)
#A warehouse feed sent you stock counts. Some are junk (negative = corrupt). Loop through the list and:

#count how many valid (zero or positive) entries there are
#sum up the total valid stock
#skip the negatives entirely

#pythonstock = [12, -4, 8, 0, -1, 25, 6]
#Expected output (print both):
#Valid entries: 5
#Total stock: 51
#Think: two counter variables before the loop, a continue to skip the bad ones (Day 4), and += to build up your totals.

stock = [12, -4, 8, 0, -1, 25, 6]
total_value = 0
count = 0

for value in stock:
    if value < 0:
        continue
    total_value += value
    count += 1

print(f"Valid entries: {count}")
print(f"Total stock: {total_value}")
'''count = 1
while count <= 3:
    print(count)
    count += 1


count_value = 5
while count_value >= 1:
    print(count_value)
    count_value -= 1
print("Done")



products = ["Mouse","Keyboard","TV","Fridge"]
n = 1
for product in products:
    print(f"{n}. {product}")
    n+=1

for i in range(1,11):
    print(i)

for i in range(2, 21, 2):
    print(i)'''


stock_counts = [12, -5, 8, -3, 20, 0, 99, 45]

for count in stock_counts:
    if count == 0:
        break
    if count < 0:
        continue
    print(count)
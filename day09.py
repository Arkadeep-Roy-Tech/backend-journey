# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price

# mouse = Product("Mouse", 499)
# tv = Product("TV", 25000)
# print(tv.name)
# print(mouse.name)

# class Product:
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity

#     def total_value(self):
#         return self.price * self.quantity

#     def apply_discount(self, percent):
#         return round(self.price - (self.price * percent / 100), 2)

# mouse = Product("Mouse", 499, 30)
# tv = Product("TV", 25000, 20)

# print(mouse.apply_discount(10))
# print(tv.apply_discount(10))

# class BankAccount:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance += amount
#         return self.balance
    
#     def withdraw(self, amount):
#         if amount > self.balance:
#             return "Insufficient funds"
#         self.balance -= amount
#         return self.balance

# account = BankAccount("Arkadeep", 1000)
# print(account.deposit(1000))
# print(account.withdraw(2100))

# class Rectangle:
#     def __init__(self, height, width):
#         self.height = height
#         self.width = width
    
#     def area(self):
#         return self.width * self.height

#     def perimeter(self):
#         return 2 * (self.width + self.height)

# rectangle = Rectangle(4, 2)
# print(rectangle.area())
# print(rectangle.perimeter())

# class Student:
#     def __init__(self, name, grades):
#         self.name = name
#         self.grades = grades
    
#     def average(self):
#         total = 0
#         for individual_grade in self.grades:
#             total += individual_grade
#         avg = total / len(self.grades)
#         return round(avg, 2)
    
#     def add_grade(self, grade):
#         self.grades.append(grade)
#         return self.grades

# student = Student("Arkadeep", [15, 20, 18])
# print(student.average())
# print(student.add_grade(20))

class InventoryItem:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def is_low_stock(self, threshold):
        return self.quantity < threshold
    
    def restock(self, amount):
        self.quantity += amount
        return self.quantity
    
    def total_value(self):
        return self.price * self.quantity

item = InventoryItem("TV", 25000, 20)
print(item.is_low_stock(30))
print(item.restock(20))
print(item.is_low_stock(30))
print(item.total_value())
# ---------------------------------------------------------
# MATH & OOP PYTHON QUIZ
# ---------------------------------------------------------

# 1. Write a function named 'add' that takes two numbers and returns their sum. 
def add_numbers(a, b):
    return a + b
a = int(input('Enter First Number :'))
b = int(input('Enter Second Number :'))

total = (a + b)
print(f'Q1 sum of two numbers {a} + {b} = {total}')
 
# 2. Write a function named 'minus' that takes two numbers and returns the result.
def minus(a, b):
    return a - b
a = int(input('Enter First Number :'))
b = int(input('Enter Second Number :'))

total = (a - b)
print(f'Q2 difference of two numbers {a} - {b} = {total}')
# 3. Write a function named 'multiply' that takes two numbers and returns the result.
def minus(a, b):
    return a * b
a = int(input('Enter First Number :'))
b = int(input('Enter Second Number :'))

total = (a * b)
print(f'Q3 the product of two numbers {a} * {b} = {total}')
# 4. Write a function named 'divide' that takes two numbers and returns the result.
def divide(a, b):
    return a // b
a = int(input('Enter First Number :'))
b = int(input('Enter Second Number :'))

total = (a // b)
print(f'Q4 quotient of two numbers {a} // {b} = {total}')
# 5. Write a function named 'solve_y' that takes m, x, and b, and returns (m * x + b).
def solve_y(m,x,b):
    return m * x + b
m = int(input('Enter First Number :'))
x = int(input('Enter Second Number :'))
b = int(input('Enter Third Number :'))
total = (m * x + b)
print(f'Q5 the expression of three numbers {m} * {x} + {b} = {total}')
# 6. Write a function named 'square' that takes one number and returns that number times itself.
def square(a):
    return a * a
a = int(input('Enter The Number :'))
total = (a * a)
print(f'Q6 the square number {a} * {a} = {total}')


# 7. Create a class named 'MathStudent' that can store a 'name' attribute.
class MathStudent:
    def __init__(self, name):
        self.name = name
# 8. Inside the 'MathStudent' class, create a method named 'get_area' for a rectangle.
def get_area(self, length, width):
    return(length * width)
# 9. Create a class named 'Calculator' with a starting attribute 'total' set to 0.
class Calculator:
    def __init__(self):
        self.total = 0
# 10. Inside the 'Calculator' class, create a method named 'add_to_total' to update the total.
class Calculator:
    def __init__(self) :
        self.total =0
    def add_to_total(self, value):
        self.total = 0
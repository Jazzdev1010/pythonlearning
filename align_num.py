"""
Align Numbers: Write a program that takes 3 numbers as input and prints 
them in a column, right-aligned with a width of 5 characters.
"""
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
def right_align( num1, num2, num3):
    print(f"{num1:>5}")
    print(f"{num2:>5}")
    print(f"{num3:>5}")
right_align(num1,num2,num3)
number = int(input("Enter a positive number: "))
factorial = 1
while number > 0:
  factorial *= number
  number -= 1
print("Factorial:", factorial)

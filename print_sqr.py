number = int(input("Enter a number: "))
numbers = list(range(1, number + 1))

# list to store the squares
squares = []

# calculate the square of each number 
for num in numbers:
  squares.append(num**2)
print("Nums:|Sqrs:")

# print in a formatted way
for i in range(len(numbers)):
  print(f"{numbers[i]}^{2} = {squares[i]}")

num = int(input("Enter a number: "))
is_prime = True
if num <= 1:
  is_prime = False
elif num <= 3:
  is_prime = True
elif num % 2 == 0 or num % 3 == 0:
  is_prime = False
else:
  for i in range(5, int(num**0.5) + 1, 6):
    if num % i == 0 or num % (i + 2) == 0:
      is_prime = False
      break
print(is_prime)
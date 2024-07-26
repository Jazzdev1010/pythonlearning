num = int(input("Enter a number: "))
order = len(str(num))
sum = 0
temp = num
while temp > 0:
  digit = temp % 10
  sum += digit ** order
  temp //= 10
is_armstrong = num == sum
print(is_armstrong)

def divide(x, y):
  try:
    result = x / y
    return result
  except ZeroDivisionError:
    return "Division by zero is not allowed"

# Example usage:
print(divide(10, 2))  # Output: 5.0
print(divide(5, 0))  # Output: Division by zero is not allowed

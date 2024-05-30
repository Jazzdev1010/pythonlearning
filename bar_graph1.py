"Write a program that takes a list of numbers as input and prints a simple bar graph using asterisks (*)"
"where the length of each bar represents the value of the corresponding number."

def print_bar_graph(numbers):
  # Find the maximum value in the list
  max_value = max(numbers)

  # Iterate through each number in the list
  for num in numbers:
    # Calculate the number of asterisks
    bar_length = int(num * 20 / max_value)
    # Print the bar label (number)
    print(f"{num}: ", end="")

    # Print the asterisks for the bar
    print("*" * bar_length)

# Example usage
numbers = [3, 8, 12, 5, 10]
print_bar_graph(numbers)
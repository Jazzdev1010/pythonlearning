def numbers_to_strings(argument):
    switcher = {
        0: "zero",
        1: "one",
        2: "two"
    }
    return switcher.get(argument, "Invalid input")

print(numbers_to_strings(1))  # Output: one
print(numbers_to_strings(5))  # Output: Invalid input

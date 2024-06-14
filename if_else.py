# Print elements of a list
fruits = ["apple", "litchi", "banana", "cherry", "passion", "kiwi", "peaches","pineapple"]
print(fruits)

# Take input from user
fruit_name = input("Enter a fruit name: ")

# conditions
if fruit_name == "passion":
    print("This fruit is sour in taste")
elif fruit_name == "litchi" and fruit_name == "pineapple":
    print("This fruit has tentacles in Rind")
else:
    print("This fruit is sweet in taste")
    
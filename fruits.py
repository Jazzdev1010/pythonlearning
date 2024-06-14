fruits = {
    "lemon": "sour",
    "lime": "sour",
    "grapefruit": "sour",
    "apple": "sweet",
    "mango": "sweet",
    "orange": "sweet",
    "strawberry": "sweet",
    "watermelon": "sweet",
}

fruit_name = input("Enter a fruit name: ").lower()  # Convert input to lowercase for case-insensitivity

if fruit_name in fruits:
    taste = fruits[fruit_name]
    print(f"{fruit_name.capitalize()} is {taste}.")  # Capitalize the first letter of the fruit name
else:
    print(f"Sorry, I don't know if {fruit_name} is sour or sweet.")
fruits = {
    "apple": {
        "color": "red",
        "taste": "sweet",
        "nutrients": ["vitamin C", "fiber"]
    },
    "orange": {
        "color": "orange",
        "taste": "sweet and tangy",
        "nutrients": ["vitamin C", "potassium"]
    },
    "mango": {
        "color": "yellow",
        "taste": "sweet",
        "nutrients": ["vitamin A", "fiber"]
    }
}

def get_fruit_info(fruit_name):
  if fruit_name in fruits:
    return fruits[fruit_name]
  else:
    return None

fruit_to_find = "apple"
fruit_info = get_fruit_info(fruit_to_find)

if fruit_info:
  print(f"Information about {fruit_to_find}:")
  for key, value in fruit_info.items():
    print(f"{key}: {value}")
else:
  print(f"{fruit_to_find} not found in the dictionary.")

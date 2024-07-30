def get_fruit(fruit_code):
    match fruit_code:
        case 1:
            return "Apple"
        case 2:
            return "Banana"
        case 3:
            return "Orange"
        case _:
            return "Unknown fruit"

print(get_fruit(2)) 
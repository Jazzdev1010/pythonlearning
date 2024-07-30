shape = input("Enter a Shape:")
radius = 7
print("Radius is fixed, 7cm")

match shape:
    case "circle":
        area = 3.14159 * radius**2
        print(f"Area of circle: {area}")
    case "rectangle":
        length = 4
        width = 5
        area = length * width
        print(f"Area of rectangle: {area}")
    case _:
        print("Invalid shape")

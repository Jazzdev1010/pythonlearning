color = input("Enter a color:")

match color:
    case "red":
        print("Stop")
    case "yellow":
        print("Caution")
    case "green":
        print("Go")
    case _:
        print("Invalid color")

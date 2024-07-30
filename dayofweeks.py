day = input("Enter a Day:")

match day:
    case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
        print("Weekday! Keep up the good work.")
    case "Saturday" | "Sunday":
        print("Weekend! Have grate fun!")
    case _:
        print("Invalid day")

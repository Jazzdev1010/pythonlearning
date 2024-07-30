
grade = input("Enter a Grade:")

match grade:
    case 'A':
        print("Excellent! You did greate!")
    case 'B':
        print("Good! You are doing good. Keep improving.")
    case 'C':
        print("Average! You need to improve your grade. Keep studying.")
    case _:
        print("Failed! You need to retake the exam.")

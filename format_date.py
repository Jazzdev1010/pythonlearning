from datetime import datetime

# Get the date string as input
date_str = input("Enter a date in YYYY-MM-DD format (Exp: 2024-03-25): ")

# Parse the date string into a datetime object
try:
  date_obj = datetime.strptime(date_str, "%Y-%m-%d")
except ValueError:
  print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
  exit()

# Format the date object into the desired format ("Month dd, YYYY")
formatted_date = date_obj.strftime("%B %d, %Y")

# Print the formatted date
print(formatted_date)
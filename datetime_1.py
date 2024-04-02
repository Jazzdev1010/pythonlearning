from datetime import datetime
def format_date(date_str):
  try:
    date_obj = datetime.strptime(date_str, "%Y-%m-%d")
    formatted_date = date_obj.strftime("%B %d, %Y")
    return formatted_date
  except ValueError:
    print("Invalid date format. Please enter a date in YYYY-MM-DD format.")
    return None
date_input = input("Enter a date in YYYY-MM-DD format (like: 2024-04-02): ")
formatted_date = format_date(date_input)
if formatted_date:
  print(formatted_date)

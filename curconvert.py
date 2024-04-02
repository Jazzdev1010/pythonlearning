usd_amt = float(input("Enter the amount in USD: "))
exchange_rate = float(input("Enter the exchange rate: "))
converted_amt = usd_amt * exchange_rate

print(f"{usd_amt} USD is equivalent to {converted_amt:} INR")
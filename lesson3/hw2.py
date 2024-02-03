"""
Here is the formula to calculate total bill:
Tip Amount = Bill Amount x Tip Percent Converted to Decimal
Bill Total = Bill Amount + Tip Amount
"""

# take entry and do conversion
bill = float(input("Bill Amount:"))
percent = float(input("Tip Percentage:")) / 100

# calculating the tip and the total
tip = bill * percent
total = round(bill + tip, 2)

# printing the total bill
print(f"Total to Pay: {total}")

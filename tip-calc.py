def total_plus_tip(bill, percentage):
    return bill + (bill * (percentage / 100))

print("TIP CALCULATOR\n\n")
bill = float(input("\nWhat was the total bill?\n"))
tip = float(input("\nWhat percentage you want to tip?\n"))
people = int(input("\nSplit the bill?\n"))

print(f"Total: {round(total_plus_tip(bill, tip), 2)}")
print(f"Per person: {round(total_plus_tip(bill, tip), 2) / people}")


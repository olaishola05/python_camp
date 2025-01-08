print("Welcome to the tip calculator.")

total_bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip do you want to give? 10, 12, or 15? "))
number_of_split = int(input("How many people to split the bill? "))

bill_with_tip = tip / 100 * total_bill + total_bill  # Or bill * (1 + tip/100)
bill_per_person = round((bill_with_tip / number_of_split), 2)

bill_per_person = "{:.2f}".format(bill_with_tip / number_of_split)
print(f"Each person should pay: ${bill_per_person}")

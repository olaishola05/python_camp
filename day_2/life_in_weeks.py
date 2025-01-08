age = input("What is your current age: ")
MAX_AGE = 120

int_age = int(age)

age_diff = MAX_AGE - int_age

remaining_days = age_diff * 365
remaining_months = age_diff * 12
remaining_weeks = age_diff * 52


message = f"You have {remaining_days} days, {remaining_weeks} weeks, and {remaining_months} months left"

print(message)

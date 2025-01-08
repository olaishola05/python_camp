height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

bmi = round(weight / height**2)
# bmi_in_int = int(bmi)

if bmi < 18.5:
    print(f"Your bmi is {bmi}, you are underweight")
elif bmi < 25:
    print(f"Your bmi is {bmi}, you are a normal weight")
elif bmi < 30:
    print(f"Your bmi is {bmi}, you are overweight")
elif bmi < 35:
    print(f"Your bmi is {bmi}, you are obese")
else:
    print(f"Your bmi is {bmi}, you are clinical obese.")

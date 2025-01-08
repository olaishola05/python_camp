print("Welcome to you Usual Sunday Pizza Joint")

size = input("What size of pizza do you want? L, M, S: ")
add_pepperoni = input("Do you want pepperoni? Y or N: ")
add_cheese = input("Do you want cheese? Y or N: ")

ORDER_BILL = 0

if size == "L":
    ORDER_BILL = 25
elif size == "M":
    ORDER_BILL = 20
elif size == "S":
    ORDER_BILL = 15
else:
    ORDER_BILL += 25

if add_pepperoni == "Y":
    if size == "S":
        ORDER_BILL += 2
    else:
        ORDER_BILL += 3
if add_cheese == "Y":
    ORDER_BILL += 1

print(f"Your final bill is: ${ORDER_BILL}")

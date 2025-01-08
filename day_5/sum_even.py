TOTAL = 0

for number in range(1, 101):
    if number % 2 == 0:
        TOTAL += number

# alternative solution
TOTAL2 = 0
for number in range(2, 101, 2):
    TOTAL2 += number

print(TOTAL2)

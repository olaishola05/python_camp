row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]

mapList = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to put the treasure? ")

column = int(position[0])
row = int(position[1])

# selected_row = mapList[row - 1]
# selected_row[column - 1] = "X"

mapList[row - 1][column - 1] = "X"


print(f"{row1}\n{row2}\n{row3}")

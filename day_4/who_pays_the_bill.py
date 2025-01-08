import random as r

names_string = input("Give me everybody's names, separated by a comma. ")

friends = names_string.split(", ")
print(friends)

who_pays = r.randint(0, len(friends) - 1)


print(f"{friends[who_pays]} is going to buy the meal today!")

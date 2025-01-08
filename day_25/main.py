# with open('weather-data.csv') as weather_file:
#     data = weather_file.readlines()
#     print(data)

# import csv
#
# with open("weather-data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#     print(temperature)
#     # print(row[2])

import pandas

# data = pandas.read_csv("weather-data.csv")  # Whole table data is called dataFrame

# Getting column data
# temp = data["temp"]  # every column is called a series
# temp_list = data["temp"].to_list()  # Either get column using bracket notations
# average = data.temp.mean()  # Or by using dot notation
# max_temp = temp.max()
# print(average)


# Getting row data

# row_dot_notation = data[data.day == "Monday"]
# monday_temp = int(row_dot_notation.temp)
# to_fehrent = monday_temp * 9/5 + 32
# print(to_fehrent)

# row_bracket_notation = data[data["day"] == "Monday"]
# row_max = data[data.temp == data.temp.max()]
# print(row_max)

# Creating DataFrame from scratch

# students_dict = {
#     "students": ["Anna", "Tyrone", "Debbie"],
#     "scores": [76, 45, 89]
# }

# new_data = pandas.DataFrame(students_dict)
# print(new_data)
# print(new_data.students.to_list())
# print(new_data[new_data.scores == new_data.scores.max()])
#
# new_data.to_csv("students_record.csv")

quote = pandas.read_csv("Central_Park_Squirrel_Census_Data.csv")
colors = quote["Primary Fur Color"]
gray = len(quote[colors == "Gray"])
cinnamon = len(quote[colors == "Cinnamon"])
black = len(quote[colors == "Black"])

new_data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray, cinnamon, black]
}

df = pandas.DataFrame(new_data_dict)
df.to_csv("squirrel_count.csv")


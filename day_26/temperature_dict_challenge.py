weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

# celcious_to_fehrent = temp * 9 / 5 + 32 # formula

weather_f = {day: (temp_c * 9 / 5) + 32 for (day, temp_c) in weather_c.items()}

print(weather_f)

# {'Monday': 53.6, 'Tuesday': 57.2, 'Wednesday': 59.0, 'Thursday': 57.2, 'Friday': 69.8, 'Saturday': 71.6,
# 'Sunday': 75.2}

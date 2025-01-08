students_dict = {
    "student": ["Sam", "Moses", "Noah"],
    "score": [80, 90, 78]
}

import pandas

students_data_frame = pandas.DataFrame(students_dict)
print(students_data_frame)

for (key, value) in students_data_frame.items():
    # print(value)
    pass
# Looping through rows in pandas iterrows

for (index, row) in students_data_frame.iterrows():
    # print(row.scores)
    if row.student == "Sam":
        print(row.score)
student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

student_grades = {}


def auto_grading(scores):
    for key in student_scores:
        score = scores[key]
        """ if score <= 70:
            student_grades[key] = "Fail"
        elif score in range(71, 80):
            student_grades[key] = "Acceptable"
        elif score in range(81, 90):
            student_grades[key] = "Exceed Expectationss"
        else:
            student_grades[key] = "Outstanding" """

        if score > 90:
            student_grades[key] = "Outstanding"
        elif score > 80:
            student_grades[key] = "Exceeds Expectations"
        elif score > 70:
            student_grades[key] = "Acceptable"
        else:
            student_grades[key] = "Fail"


auto_grading(student_scores)
print(student_grades)

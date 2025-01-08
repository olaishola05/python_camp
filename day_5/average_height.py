student_heights = input("Input a List of student heights ").split()

# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])

NUMBER_OF_STUDENTS = 0
TOTAL_STUDENT_HEIGHTS = 0

for height in student_heights:
    TOTAL_STUDENT_HEIGHTS += int(height)
    NUMBER_OF_STUDENTS += 1

average_student_heights = round(TOTAL_STUDENT_HEIGHTS / NUMBER_OF_STUDENTS)

print(average_student_heights)

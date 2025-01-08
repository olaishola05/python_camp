student_scores = input("Input List of student scores: ").split()

for idx in range(0, len(student_scores)):
    student_scores[idx] = int(student_scores[idx])


print(student_scores)

HIGHEST_SCORE = 0

for score in student_scores:
    if score > HIGHEST_SCORE:
        HIGHEST_SCORE = score

print(HIGHEST_SCORE)

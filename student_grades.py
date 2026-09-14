students = [
    ["Samuel", 80, 75, 90],
    ["David", 55, 60, 50],
    ["Mary", 35, 40, 30],
    ["John", 65, 70, 68]
]

for student in students:
    name = student[0]
    grades = student[1:]
    total = 0

    for grade in grades:
        total += grade

    average = total / len(grades)

    if average >= 70:
        letter_grade = "A"
    elif average >= 60:
        letter_grade = "B"
    elif average >= 50:
        letter_grade = "C"
    elif average >= 45:
        letter_grade = "D"
    elif average >= 40:
        letter_grade = "E"
    else:
        letter_grade = "F"

    print(f"{name} - Average: {average:.2f} - Grade: {letter_grade}")

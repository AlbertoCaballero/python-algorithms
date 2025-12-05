student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

def grade(score):
    classified = ""
    if score >= 91 and score <= 100:
        classified = "Outstanding"
    elif score >= 81 and score <= 90:
        classified = "Exceeds Expectations"
    elif score >= 71 and score <= 80:
        classified = "Acceptable"
    elif score <= 70:
        classified = "Fail"
    return classified

student_grades = {}
for student in student_scores:
    student_grades[student] = grade(student_scores[student])


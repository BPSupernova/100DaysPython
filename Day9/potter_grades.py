student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

student_grades = {}

for key in student_scores:
  if student_scores[key] < 71:
    student_grades[key] = "Fail"
  elif student_scores[key] < 81:
    student_grades[key] = "Acceptable"
  elif student_scores[key] < 91:
    student_grades[key] = "Exceeds Expectations"
  else:
    student_grades[key] = "Outstanding"

print(student_grades)
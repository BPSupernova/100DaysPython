# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

sum = 0
length = 0

for student in student_heights:
  sum += student
  length += 1

print(f"total height = {sum}")
print(f"number of students = {length}")
print(f"average height = {round(sum / length)}")
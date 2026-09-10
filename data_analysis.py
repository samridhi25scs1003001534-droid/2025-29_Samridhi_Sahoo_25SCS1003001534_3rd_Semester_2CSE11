import csv

with open("data/students.csv", "r") as file:
    students = list(csv.DictReader(file))

print("===== DETAILED ANALYSIS =====")

# Highest and lowest scores
highest = max(students, key=lambda x: int(x["Final_Score"]))
lowest = min(students, key=lambda x: int(x["Final_Score"]))

print("\nHighest Score:")
print(highest["Student_ID"], "-", highest["Final_Score"])

print("\nLowest Score:")
print(lowest["Student_ID"], "-", lowest["Final_Score"])

# Calculate pass percentage
passed = 0

for student in students:
    if int(student["Final_Score"]) >= 60:
        passed += 1

pass_percentage = (passed / len(students)) * 100

print("\nPass Percentage:", round(pass_percentage, 2), "%")

# Attendance and performance comparison
print("\nStudents with good attendance and score:")

for student in students:
    if int(student["Attendance"]) >= 85 and int(student["Final_Score"]) >= 80:
        print(
            student["Student_ID"],
            "| Attendance:", student["Attendance"],
            "| Score:", student["Final_Score"]
        )

import csv

# Read student data from CSV file
with open("data/students.csv", "r") as file:
    students = list(csv.DictReader(file))

print("=" * 50)
print("       STUDENT PERFORMANCE ANALYSIS")
print("=" * 50)

# Total number of students
total_students = len(students)

# Calculate totals
total_score = 0
total_attendance = 0
total_study_hours = 0

for student in students:
    total_score += int(student["Final_Score"])
    total_attendance += int(student["Attendance"])
    total_study_hours += int(student["Study_Hours"])

# Calculate averages
average_score = total_score / total_students
average_attendance = total_attendance / total_students
average_study_hours = total_study_hours / total_students

print("\n--- OVERALL PERFORMANCE ---")
print("Total Students:", total_students)
print("Average Final Score:", round(average_score, 2))
print("Average Attendance:", round(average_attendance, 2), "%")
print("Average Study Hours:", round(average_study_hours, 2))

# Find highest scorer
top_student = max(students, key=lambda x: int(x["Final_Score"]))

print("\n--- TOP PERFORMER ---")
print("Student ID:", top_student["Student_ID"])
print("Final Score:", top_student["Final_Score"])

# Performance categories
excellent = 0
good = 0
average = 0
needs_improvement = 0

for student in students:
    score = int(student["Final_Score"])

    if score >= 90:
        excellent += 1
    elif score >= 75:
        good += 1
    elif score >= 60:
        average += 1
    else:
        needs_improvement += 1

print("\n--- PERFORMANCE DISTRIBUTION ---")
print("Excellent:", excellent)
print("Good:", good)
print("Average:", average)
print("Needs Improvement:", needs_improvement)

# Attendance analysis
low_attendance = 0

for student in students:
    if int(student["Attendance"]) < 75:
        low_attendance += 1

print("\n--- ATTENDANCE ANALYSIS ---")
print("Students below 75% attendance:", low_attendance)

# Study hours analysis
high_study_hours = 0

for student in students:
    if int(student["Study_Hours"]) >= 6:
        high_study_hours += 1

print("\n--- STUDY HABIT ANALYSIS ---")
print("Students studying 6+ hours:", high_study_hours)

# Find students needing improvement
print("\n--- STUDENTS NEEDING IMPROVEMENT ---")

for student in students:
    if int(student["Final_Score"]) < 60:
        print(
            student["Student_ID"],
            "- Score:",
            student["Final_Score"]
        )

print("\n" + "=" * 50)
print("Analysis completed successfully!")
print("=" * 50)

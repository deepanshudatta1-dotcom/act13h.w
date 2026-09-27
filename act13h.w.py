# My School Subject Planner

# 1. Store fixed student details in a tuple
student_details = ("Rahul", 20, "BCA", "Section A")

# 2. Access tuple values
print("Student Name:", student_details[0])
print("Age:", student_details[1])
print("Course:", student_details[2])
print("Section:", student_details[3])

# 3. Create subject sets for different days
monday_subjects = {"Maths", "English", "Science", "Computer"}
tuesday_subjects = {"English", "Science", "Hindi", "Computer"}

print("\nMonday Subjects:", monday_subjects)
print("Tuesday Subjects:", tuesday_subjects)

# 4. Modify sets

# Add a subject
monday_subjects.add("History")

# Remove a subject
tuesday_subjects.remove("Hindi")

print("\nAfter Modification:")
print("Monday Subjects:", monday_subjects)
print("Tuesday Subjects:", tuesday_subjects)

# 5. Common set operations

# Union - all subjects from both days
all_subjects = monday_subjects.union(tuesday_subjects)
print("\nAll Subjects:", all_subjects)

# Intersection - subjects common on both days
common_subjects = monday_subjects.intersection(tuesday_subjects)
print("Common Subjects:", common_subjects)

# Difference - subjects only on Monday
monday_only = monday_subjects.difference(tuesday_subjects)
print("Monday Only:", monday_only)

# Difference - subjects only on Tuesday
tuesday_only = tuesday_subjects.difference(monday_subjects)
print("Tuesday Only:", tuesday_only)
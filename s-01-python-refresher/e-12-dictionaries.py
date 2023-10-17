friends = {"Ana": 24, "Alexandra": 35}
friends["Eva"] = 28

print(friends)

my_friends = [
    {"name": "Rolf", "age": 28},
    {"name": "Ana", "age": 24},
    {"name": "Alexandra", "age": 35}
]
print(my_friends[1]["name"])

student_attendance = {"Matt": 86, "Ana": 91, "Alexandra": 100}

# # method 1
# for student in student_attendance:
#     print(f"{student}: {student_attendance[student]}")

# method 2
for student, attendance in student_attendance.items():
    print(f"{student}: {attendance}")

user_input = input("Enter a student name to query: ")
if user_input in student_attendance:
    print(f"{user_input}: {student_attendance[user_input]}")
else:
    print(f"{user_input} is not in this class.")

# can also extract values from dictionaries
attendance_values = student_attendance.values()
print(f"Average attendance: {sum(attendance_values) / len(attendance_values):.0f}")

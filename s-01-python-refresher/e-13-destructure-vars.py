t = 5, 11
print(type(t))

# tuples can be decoupled
x, y = t
print(x, y)

# revisiting dictionaries
student_attendance = {"Matt": 86, "Ana": 91, "Alexandra": 100}
print(list(student_attendance.items()))
# print(type(list(student_attendance.items())))

for a_tuple in student_attendance.items():
    print(a_tuple)

# use "_" to denote ignoring a variable
person = ("Ana", 29, "Data Scientist")
name, _, profession = person
print(name, profession)

# separate list into two lists
*head, tail = [1,2,3,4,5]
print("Head: ", head, "\nTail: ", tail)

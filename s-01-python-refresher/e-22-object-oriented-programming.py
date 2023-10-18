# Object Oriented Programming (OOP)
student = {"name": "Ana", "grades": (89, 90, 93, 78, 90)}

def average(sequence):
    return sum(sequence) / len(sequence)

# pass tuple to function
print(average(student["grades"]))

# representing the average function in a class is called a method
# self: convention in python
class Student:
    # __init__ method is called when class is instantiated
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average_grade(self):
        return sum(self.grades) / len(self.grades)

# instantiate the class
student = Student("Alexandra", (89, 90, 93, 78, 90))
# access the name property of student class
print(student.name)
print(student.average_grade())

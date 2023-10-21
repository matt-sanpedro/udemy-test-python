from typing import List, Optional

class Student:
    # NEVER make a parameter equal to a mutable value be default
    # as shown, the two stundent instances below share grades
    # def __init__(self, name: str, grades: List[int] = []): # this is bad

    # optional list of integers, may be None initially
    def __init__(self, name: str, grades: Optional[List[int]] = None): # this is bad
        self.name = name
        self.grades = grades or [] # None will evaluate to grades or empty list

    def take_exam(self, result: int):
        self.grades.append(result)

ana = Student("Ana")
amber = Student("Amber")
ana.take_exam(90)

# both students have 90 even though Ana took an exam
print("Ana's grades: ", ana.grades)
print("Amber's grades: ", amber.grades)

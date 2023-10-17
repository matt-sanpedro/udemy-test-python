# -- Part 1 --
"""
Modify the code so that the evens list contains only the even numbers of the numbers list.
You do not need to print anything.
"""
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

evens = []
for number in numbers:
    if number % 2 == 0:
        evens.append(number)
# print(evens)

# -- Part 2, must be completed before submitting! --
"""
For part 2, add a clause to the if statement such that if the user's input is "q", 
your program prints "Quit".
"""
user_input = input("Enter your choice: ")
if user_input == "a":
    print("Add")
elif user_input == "q":
    print("Quit")
    
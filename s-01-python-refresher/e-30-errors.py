def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0.")
    
    return dividend / divisor

# divide(15, 0)

# grades = [78, 99, 85, 100]
grades = [59.5, 44.5, 80, 76.5, 91]
# grades = ['a']
# grades = []

print("Welcome to the average grade program.")

# use try except to catch errors
try: 
    average = divide(sum(grades), len(grades))
    # print(f"The average grade is {average}.")
except ZeroDivisionError as e:
    print(f"Error: {e}")
    print("There are no grades yet in your list.")
except TypeError:
    print("List of integers expected for grades.")
else:
    print(f"The average grade is {average}.")
finally:
    # this block will ALWAYS execute
    print("Thank you for using the program!")
# arguments provide values to parameters x and y
def add(x, y):
    return x + y

print(add(4,5))

# positional arguments: it's order will effect the assigned parameter
def say_hello(name, surname):
    print(f"Hello {name}, {surname}")

say_hello("Alexandra", "Daddario")
say_hello(surname="Daddario", name="Alexandra")

# good practice: no spaces between variables when assign values to functions
# BAD practice: returning different data types for the function
def divide(dividend, divisor):
    if divisor != 0:
        print(dividend / divisor)
    else:
        print("You fool!")

divide(dividend=15, divisor=0)

# NOTE: positional argument order
# divide(dividend=15,0) # SyntaxError: positional arguments follow keyword argument
divide(15,divisor=0)

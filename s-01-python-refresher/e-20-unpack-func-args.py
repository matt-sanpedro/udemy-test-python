# args: variable name to collect arguments
def multiply(*args):
    print(args) # prints a tuple of tuples, example: ((3, 6, 1),)
    total = 1
    for arg in args: total *= arg
    return total

print(multiply(1, 3, 5)) # will print out as a tuple

# operator: creates a compulsory named argument
def apply(*args, operator):
    if operator == "*":
        return multiply(*args) # asterisk needed to pass in the values as individual numbers
    elif operator == "+":
        return sum(args)
    else:
        return "No valid operator provided to apply()."

print("SOLUTION: ", apply(3, 6, 1, operator="*"))

# destructuring with asterisk
def add(x, y):
    return x + y

nums = [3, 5]
print(add(*nums))

# two asterisks will pass in a dictionary with associated keys
nums = {"x": 15, "y": 25}
print(add(x=nums["x"], y=nums["y"]))
print(add(**nums))

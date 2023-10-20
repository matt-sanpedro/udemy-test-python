from operator import itemgetter

# First class functions: functions that are variables

# EXAMPLE 1: divide as a first class function
def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0.")

    return dividend / divisor

# operator is a mandatory value
def calculate(*values, operator):
    # print(type((values[0], values[1])))
    return operator(*(values[0], values[1]))

# can pass a first class function "divide" as an argument to another function
result = calculate(20, 2, operator=divide)
print(result)

# EXAMPLE 2: search function
def search(sequence, expected, finder):
    for elem in sequence:
        if finder(elem) == expected:
            return elem
    raise RuntimeError(f"Could not find an element with {expected}")

freinds = [
    {"name": "Matt", "age": 30},
    {"name": "Alexandra", "age": 37},
    {"name": "Ana", "age": 28}
]

def get_friend_name(friend):
    print(f"Searching: {friend['name']}")
    return friend["name"]

# METHOD 1: defined function
print(search(freinds, "Alexandra", get_friend_name))
# METHOD 2: lambda function
print(search(freinds, "Alexandra", lambda friend: friend["name"]))
# METHOD 3: function that creates other functions, "itemgetter"
print(search(freinds, "Alexandra", itemgetter("name")))

def named(**kwargs):
    print(kwargs)

named(name="Ana", age=24)

def snake(name, age):
    print(name, age)

details = {"name": "Alexandra", "age": 25}
snake(**details)

def print_nicely(**kwargs):
    named(**kwargs)

    for arg, value in kwargs.items():
        print(f"{arg}: {value}")

print_nicely(name="Amber", age=31)

# can pass tuples and dictionary types to functions
def both(*args, **kwargs):
    print(args)
    print(kwargs)

both(1, 3, 5, name="Selena", age=35)

def myfunction(**kwargs):
    print(kwargs)

# myfunction(**"Alexandra") # Error, must be mapping
# myfunction(**None) # Error

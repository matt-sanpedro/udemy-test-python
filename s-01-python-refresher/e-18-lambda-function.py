# lambda function: does not have a name
def add(x, y):
    return x + y

# lambda equivalent of add function
# assigning a lambda function
add = lambda x, y: x + y
print(add(5, 7))

# executing the lambda function
print((lambda x, y: x + y)(12, 8))

# useful lambda function
def double(x):
    return x * 2

sequence = [1, 3, 5, 9]

# list comprehension is usually faster in Python but may need to compromise on code style with map
doubled = [x * 2 for x in sequence]
print(doubled)
doubled = [double(x) for x in sequence]
print(doubled)

# map goes through each element in sequence and applied the double function
# Note: map returns a object and must wrap with "list()" to return list data type
doubled = map(double, sequence)
print(list(doubled))

# better to use lambda function with map instead for better code to read
doubled = [(lambda x: x * 2)(x) for x in sequence]
print(doubled)
doubled = map(lambda x: x * 2, sequence)
print(list(doubled))

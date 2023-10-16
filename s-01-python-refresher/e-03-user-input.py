name = input("Enter your name: ")
print(f"Hello, {name}")

# the input function always returns a string, but there are several conversion functions in Python
size_input = input("How big is your house (in square feet): ")
square_feet = float(size_input)
square_meters = square_feet / 10.8
print(f"{square_feet} square feet is equivalent to {square_meters:.2f} square meters")

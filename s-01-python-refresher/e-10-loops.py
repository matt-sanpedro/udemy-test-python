# play the magic number game
number = 7

# while loops that start with "True" must terminate within to avoid infinite loop
while True:
    user_input = input("Would you like to play? (Y/n) ")

    if user_input == "n":
        break    
    
    user_number = int(input("Guess our number: "))
    if user_number == number:
        print("You guessed correctly")
        break
    # elif number - user_number in (1, -1):
    elif abs(number - user_number) == 1:
        print("You were off by one.")
    else:
        print("Sorry, it's wrong!")

# for loop
friends = ["Ana", "Alexandra", "Jen", "Filipe"]
for friend in friends:
    print(f"{friend} is my friend.")


grades = [35, 67, 98, 100, 100]
total = 0
amount = len(grades)

# method 1: add with loop
for grade in grades:
    total += grade

# method 2: use the sum function
total = sum(grades)

print(total/amount)

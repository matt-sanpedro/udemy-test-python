numbers = [1, 3, 5]
doubled = []

doubled = [x * 2 for x in numbers]
print(doubled)

# friends = ["Ana", "Taylor", "Alexandra", "Abigail"]
friends = ["Ana", "Alexandra", "Abigail"]
# start_a = [friend for friend in friends if friend[0]=="A"]
starts_a = [friend for friend in friends if friend.startswith("A")]

print(starts_a is friends)
# checking for memory id
print("friends:  ", id(friends), "\nstarts_a: ", id(starts_a))
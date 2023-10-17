# in keyword works for lists
friends = ["Ana", "Alexandra", "Jen"]
print("Jen" in friends)

# a set is defined since Movies are unique
movies_watched = {"The Matrix", "Green Book", "Titanic"}
user_movie = input("Enter something you've watched recently: ")
print(user_movie in movies_watched)

# in addition to lists and sets, in keyword works on tuple and strings
my_tuple = ("Alexandra",)
print("Alexandra" in  my_tuple)
print("Ana" in  my_tuple)

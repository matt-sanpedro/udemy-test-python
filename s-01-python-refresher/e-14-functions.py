def hello():
    print("Hello!")

# not good to shadow outer variables as shown below
friends = ["Alexandra", "Ana"]

def add_friend():
    friend_name = input("Enter your friend name: ")
    freinds = friends + [friend_name]

add_friend()
print(friends) # will always output initialized "friends"

def add_amber():
    friends.append("Amber")

add_amber()
add_amber()
add_amber()
print(friends)

users = [
    (0, "Bob", "password"),
    (1, "Ana", "ana123"),
    (2, "Alexandra", "long4assword"),
    (3, "Amber", "1234")
]

# log in with dictionary comprehension
username_mapping = {user[1]: user for user in users}
# print(username_mapping)

username_input = input("Enter your username: ")
password_input = input("Enter your password: ")
_, username, password = username_mapping[username_input]

if password_input == password:
    print("Your details are correct")
else:
    print("You details are incorrect")
    
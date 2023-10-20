# secure the get_admin_password
user = {"username": "matt", "access_level": "guest"}

def get_admin_password():
    return "1234"

# not a good option to secure pass
def secure_get_admin():
    if user["access_level"] == "admin":
        return "1234"

# define a function that accepts a function as argument
def make_secure(func):
    def secure_function():
        if user["access_level"] == "admin":
            # returns calling the original function
            return func()
        else:
            return f"No admin permissions for {user['username']}."
    
    # return the function, not the function call
    return secure_function
    

# print(secure_get_admin())
# print(get_admin_password())

get_admin_password = make_secure(get_admin_password)
print(get_admin_password())

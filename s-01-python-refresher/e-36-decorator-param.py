import functools

# secure the get_admin_password
user = {"username": "matt", "access_level": "admin"}

# define a function that accepts a function as argument
# make_secure function is called a "decorator" 
# GOOD practice: with decorators, they should take an unlimited arguments
def make_secure(func):
    # this functools decorator tells python that secure_function is a wrapper
    # secure_function is not a decorator, it replaces a function
    @functools.wraps(func)
    def secure_function(*args, **kwargs):
        print("ARGUMENTS: ", *args, **kwargs)
        if user["access_level"] == "admin":
            # returns calling the original function with NO arguments
            return func(*args, **kwargs)
        else:
            return f"No admin permissions for {user['username']}."
    
    # return the function, not the function call
    return secure_function
    
# adding the "@" symbol will prevent the function from running as is
# instead, it will run the function through make_secure

@make_secure
def get_password(panel):
    print("PANEL: ", panel)
    if panel == "admin":
        return "1234"
    elif panel == "billing":
        return "super_secure_password"

# since "secure_function" is outputted, documentation attached to get_admin_password would get lost
print(get_password.__name__) # get_password is returned due to wrapper
print(get_password("billing"))

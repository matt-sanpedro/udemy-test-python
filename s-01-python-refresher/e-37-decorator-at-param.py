import functools

# secure the get_admin_password
user = {"username": "matt", "access_level": "guest"}

# define a function that accepts a function as argument
# make_secure function is called a "decorator" 
# GOOD practice: with decorators, they should take an unlimited arguments

# create a function "decorator" that will return the decorator and allow "access_level" argument
# make_secure is now a factory function (a function used to create a decorator)
def make_secure(access_level):
    # print("MAKE_SECURE: ", access_level)
    def decorator(func):
        # print("USER: ", user)
        # this functools decorator tells python that secure_function is a wrapper
        # secure_function is not a decorator, it replaces a function
        @functools.wraps(func)
        def secure_function(*args, **kwargs):
            # print("ARGUMENTS: ", *args, **kwargs)
            if user["access_level"] == access_level:
                # returns calling the original function with NO arguments
                return func(*args, **kwargs)
            else:
                return f"No {access_level} permissions for {user['username']}."
        
        # return the function, not the function call
        return secure_function
    return decorator

@make_secure("admin")
def get_admin_password():
    return "admin: 1234"

@make_secure("user")
def get_dashboard_password():
    return "user: user_password"

# test with user defined above
print(get_admin_password())
print(get_dashboard_password())

# changing the user variable defined above
user = {"username": "anna", "access_level": "admin"}
print(get_admin_password())
print(get_dashboard_password())

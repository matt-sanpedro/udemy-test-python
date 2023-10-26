"""
app notes
 
- tests for this do not belong in either unit or integration tests
- interacts with the whole system, thus belongs in system test
"""
# in python, when variable is ALL uppercase, should not change this CONSTANT
MENU_PROMPT = "Enter:\n\t'c': create a blog\n\t'l' to list blogs\n\t'r' to read one\n\t'p' to create a post\n\t'q' to quit\nYour choice: "
# creates a new dictionary
blogs = dict() # blog_name : Blog object
# blogs = {}

def menu():
    # show the user the available blogs
    print_blogs()

    # let user make a choice
    selection = input(MENU_PROMPT)
    # print(f"You entered: {selection}")

    # do something with that choice
    # eventually exit
    # include a while loop for user to exit

def print_blogs():
    # print the available blogs
    for key, blog in blogs.items(): # [(blog_name, Blog), (blog_name, Blog)]
        print(f"- {blog}")
        
menu()
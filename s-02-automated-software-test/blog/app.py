"""
app notes
 
- tests for this do not belong in either unit or integration tests
- interacts with the whole system, thus belongs in system test
"""
# creates a new dictionary
blogs = dict() # blog_name : Blog object
# blogs = {}

def menu():
    # show the user the available blogs
    # let  user make a choice
    # do something with that choice
    # eventually exit
    print_blogs()

def print_blogs():
    # print the available blogs
    for key, blog in blogs.items(): # [(blog_name, Blog), (blog_name, Blog)]
        print(f"- {blog}")
        
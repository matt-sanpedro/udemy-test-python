"""
app notes
 
- tests for this do not belong in either unit or integration tests
- interacts with the whole system, thus belongs in system test
"""
from blog import Blog

# in python, when variable is ALL uppercase, should not change this CONSTANT
MENU_PROMPT = "Enter:\n\t'c': create a blog\n\t'l' to list blogs\n\t'r' to read one\n\t'p' to create a post\n\t'q' to quit\nYour choice: "
POST_TEMPLATE = "--- {} ---\n{}\n"
# creates a new dictionary
blogs = dict() # blog_name : Blog object
# blogs = {}

def menu():
    # show the user the available blogs
    print_blogs()

    # let user make a choice
    selection = get_user_input()
    # print(f"You entered: {selection}")

    while selection != "q":
        if selection == "c":
            ask_create_blog()
        elif selection == "l":
            print_blogs()
        elif selection == "r":
            ask_read_blog()
        elif selection == "p":
            ask_create_post()
        selection = input(MENU_PROMPT)
            
    # do something with that choice
    # eventually exit
    # include a while loop for user to exit

def print_blogs():
    # print the available blogs
    for key, blog in blogs.items(): # [(blog_name, Blog), (blog_name, Blog)]
        print(f"- {blog}")
        
def get_user_input():
    return input(MENU_PROMPT)

def ask_create_blog():
    # ask user for new blog title and user name, then create the new blog and store in dict
    title = input("Enter the blog title: ")
    author = input("Enter user name: ")
    blogs[title] = Blog(title, author)

def ask_read_blog():
    # ask for a blog title, then print the post
    title = input("Enter the blog title you want to read: ")
    print_posts(blogs[title])

def print_posts(blog):
    # print the post(s) in the blog
    for post in blog.posts:
        print_post(post)
        
def print_post(post):
    # prints the title and content attributes of object
    print(POST_TEMPLATE.format(post.title, post.content))

def ask_create_post():
    # ask for blog title, post title, and post content, 
    # then create a new post in the blog specified by title
    blog_name = input("Enter the blog title youwant to write a post in: ")
    title = input("Enter your post title: ")
    content = input("Enter your post content: ")

    blogs[blog_name].create_post(title, content)

if __name__ == "__main__":
    menu()
    
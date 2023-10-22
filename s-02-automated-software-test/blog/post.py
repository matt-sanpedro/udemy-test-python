"""
in any blog assume post has two attributes: title and content
can also have metadata, author, images, etc.
good to start with simple test then progress as code grows
"""
class Post:
    def __init__(self, title, content):
        self.title = title
        self.content = content

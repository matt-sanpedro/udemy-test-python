"""
in any blog assume post has two attributes: title and content
can also have metadata, author, images, etc.
good to start with simple test then progress as code grows
"""
class Post:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def __repr__(self):
        return f"<Post {self.title}, Content: {self.content}>"

    # scenario: testing for dictionaries saved to mongoDB or SQL database
    # trailing comma: allows for creation of new line
    def json(self):
        return {
            "title": self.title,
            "content": self.content,
        }
    
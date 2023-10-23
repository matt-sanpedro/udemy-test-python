"""
Test Drive Development:
- think about what you are going to implement before you do
- point: write a test that fails but conveys what you want to do, then write method
- test one permutation and create more as you go
"""

from unittest import TestCase
from blog import Blog

class BlogTest(TestCase):
    # blog depends on post to run this integration test
    def test_create_post_in_blog(self):
        b = Blog("Test", "Test Author")
        b.create_post("Test Post", "Test Content")

        # blog list changed
        self.assertEqual(len(b.posts), 1)
        self.assertEqual(b.posts[0].title, "Test Post")
        self.assertEqual(b.posts[0].content, "Test Content")

    def test_json_no_posts(self):
        b = Blog("Test", "Test Author")
        expected = {"title": "Test", "author": "Test Author", "posts": []}

        self.assertDictEqual(expected, b.json())

    def test_json(self):
        b = Blog("Test", "Test Author")
        b.create_post("Test Post", "Test Content")

        expected = {
            "title": "Test", 
            "author": "Test Author", 
            "posts": [
                {
                    "title": "Test Post", 
                    "content": "Test Content"
                }
            ]
        }

        self.assertEqual(expected, b.json())

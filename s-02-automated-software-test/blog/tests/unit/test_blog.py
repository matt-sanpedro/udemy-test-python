"""
Test Drive Development:
- think about what you are going to implement before you do
- point: write a test that fails but conveys what you want to do, then write method
- test one permutation and create more as you go
"""

from unittest import TestCase
from blog import Blog

class BlogTest(TestCase):
    def test_create_blog(self):
        b = Blog("Test", "Test Author")

        self.assertEqual("Test", b.title)
        self.assertEqual("Test Author", b.author)
        self.assertListEqual([], b.posts)
        self.assertEqual(0, len(b.posts))

    def test_repr(self):
        b = Blog("Test", "Test Author")
        b2 = Blog("My Day", "Alexandra")

        self.assertEqual(b.__repr__(), "Test by Test Author (0 posts)")
        self.assertEqual(b2.__repr__(), "My Day by Alexandra (0 posts)")

    def test_repr_multiple_posts(self):
        b = Blog("Test", "Test Author")
        b.posts = ["test"]
        b2 = Blog("My Day", "Alexandra")
        b2.posts = ["I", "Feel", "Witty"]
        self.assertEqual(b.__repr__(), "Test by Test Author (1 post)")
        self.assertEqual(b2.__repr__(), "My Day by Alexandra (3 posts)")
        
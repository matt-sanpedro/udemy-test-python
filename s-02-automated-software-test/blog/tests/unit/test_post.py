"""
unit test purpose:
for any methods or function that don't depend on anything else 

NOTES:
- TestCase: is a part of the unittest library that PostTest inherits
- Tests ensures that as system changes, there are guidelines on how system should work
- If writing a test is too hard, then what you are testing is too complex
"""
import unittest
from post import Post

class PostTest(unittest.TestCase):
    def test_create_post(self):
        p = Post("Test", "Test Content")

        # make sure string "Test" and the title are same
        # note: this test will fail if __init__ method is changed
        self.assertEqual("Test", p.title)
        self.assertEqual("Test Content", p.content)

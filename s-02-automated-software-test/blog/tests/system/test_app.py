# system test is a larger integration test that will test entire system
from unittest import TestCase
from unittest.mock import patch # patch allows look from outside
import app
from blog import Blog

class AppTest(TestCase):
    def test_print_blogs(self):
        # test printing to console by patching the print statement
        # create the blog instant to test against
        blog = Blog("Test", "Test Author")
        app.blogs = {"Test": blog}

        # patch in the builtin print method, it likes to receive the module
        with patch("builtins.print") as mocked_print:
            app.print_blogs()
            # NOTE: uncommenting any of the print functions below will cause test to fail
            # print(mocked_print)
            # print("APP:  ", app.print_blogs())
            # print("type: ", type(app.print_blogs()))
            mocked_print.assert_called_with("- Test by Test Author (0 posts)")
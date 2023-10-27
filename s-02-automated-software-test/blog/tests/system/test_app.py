# system test is a larger integration test that will test entire system
from unittest import TestCase
from unittest.mock import patch # patch allows look from outside
import app
from blog import Blog

class AppTest(TestCase):
    
    def test_menu_prints_prompt(self):
        with patch("builtins.input", return_value = "q") as mocked_input:
            app.menu()
            mocked_input.assert_called_with(app.MENU_PROMPT)
            
    def test_menu_calls_print_blogs(self):
        with patch("app.print_blogs") as mocked_print_blogs:
            with patch("builtins.input", return_value = "q"):
                app.menu()
                mocked_print_blogs.assert_called()
            
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

    def test_user_input(self):
        # test the input q to ensure user can exit
        with patch("builtins.input"):
            expected = app.get_user_input().return_value = "q"
            self.assertEqual(expected, "q")
            
    def test_ask_create_blog(self):
        with patch("builtins.input") as mocked_input:
            # in patching, instead of returning a single value, can call side_effect
            mocked_input.side_effect = ("Test", "Test Author")
            app.ask_create_blog()
            self.assertIsNotNone(app.blogs.get("Test"))
# system test is a larger integration test that will test entire system
from unittest import TestCase
from unittest.mock import patch # patch allows look from outside
import app
from blog import Blog
from post import Post

class AppTest(TestCase):
    def setUp(self):
        # can define in TestCase and run before each test
        blog = Blog("Test", "Test Author")
        app.blogs = {"Test": blog}
        
    def test_menu_calls_create_blog(self):
        with patch("builtins.input") as mocked_input:
            with patch("app.ask_create_blog") as mocked_ask_create_blog:
                mocked_input.side_effect = ("c", "Test Create Blog", "Test Author", "q")

                app.menu()
                
                # blog is no longer created once mocked
                # self.assertIsNotNone(app.blogs["Test Create Blog"])
                mocked_ask_create_blog.assert_called()
    
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
        # blog = Blog("Test", "Test Author")
        # app.blogs = {"Test": blog}

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
            # NOTE: multiple side effects can be added to tuple value
            mocked_input.side_effect = ("Test", "Test Author")
            app.ask_create_blog()
            # app.blogs.get("Test") -> gets the value of dict with key "Test"
            self.assertIsNotNone(app.blogs.get("Test"))
            
    def test_ask_read_blog(self):
        # blog = Blog("Test", "Test Author")
        # app.blogs = {"Test": blog}
        blog = app.blogs["Test"]

        # ask_read_blog: requires user input to return value
        with patch("builtins.input", return_value = "Test"):
            with patch("app.print_posts") as mocked_print_posts:
                app.ask_read_blog()

                # check if print blog function was called
                mocked_print_posts.assert_called_with(blog)

    def test_print_posts(self):
        blog = app.blogs["Test"]
        blog.create_post("Test Post", "Test Content")
        
        with patch("app.print_post") as mocked_print_post:
            app.print_posts(blog)
            mocked_print_post.assert_called_with(blog.posts[0])
            
    def test_print_post(self):
        # mock the print function
        post = Post("Post title", "Post content")
        expected_print = "--- Post title ---\nPost content\n"
        
        with patch("builtins.print") as mocked_print:
            app.print_post(post)
            mocked_print.assert_called_with(expected_print)
            
    def test_ask_create_post(self):
        blog = app.blogs["Test"]
        
        # mock input function
        with patch("builtins.input") as mocked_input:
            mocked_input.side_effect = ("Test", "Test Title", "Test Content")
        
            # ensure blog has new post
            app.ask_create_post()
            self.assertEqual(blog.posts[0].title, "Test Title")
            self.assertEqual(blog.posts[0].content, "Test Content")

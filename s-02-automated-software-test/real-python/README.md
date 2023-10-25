# Real Python Tutorial
- doc source: https://realpython.com/python-mock-library/
- video source: https://realpython.com/lessons/python-mock-object-library-overview/

## unittest.mock
- provides class Mock, used to imitate real objects in codebase
- also provides function patch()
    * replaces real objects in code with Mock instances
    * patch() can be implemented as either a decorator or context manager
    * once designed scoped exits, patch() will claen up code by replacing mocked objects with original counterparts

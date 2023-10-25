# Automated Software Test

## Virtual Environments Set Up and Implementation
### Linux Command Line
- create a new virtual environment:
```virtualenv venv```
- activate the virtual environment:
```source venv/bin/activate```
- deactivate the virtual environment
```deactivate```

### Windows Command Line
- create a new virtual environment:
```py -m venv venv```
- activate the virtual environment:
```.\venv\Scripts\activate```
- deactivate the virtual environment
```deactivate```

## Running Test Scripts
### Linux Command Line
- can run specific test script with command (directory of blog: post.py):
- folder structure of test py file: blog/tests/unit
- file name of test py file: test_post.py
- run a single file with: ```python3 -m unittest tests.unit.test_post```
- run all tests in directory with: ```python3 -m unittest discover <test_directory>```

### Windows Command Line
- same folder structure set up as Linux
- run a single file with: ```py -m unittest tests.unit.test_post```
- run all tests in directory with: ```py -m unittest discover <test_directory>```
- target specific scripts with VERBOSE mode from the blog directory: 
```py -m unittest tests\system\test_app.py -v```


## Research to become better at writing Python test cases
- boundary value analysis
- equivalence partitioning

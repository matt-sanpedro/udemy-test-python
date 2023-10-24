# unittest.mock, the mock object library
- allows you to replace pasrts of system under test with mock objects and make assertions
- source: https://docs.python.org/3/library/unittest.mock.html

## Introduction
- Mock and MagicMock objects create all attributes and methods as you access them and store details of how they have been used
- A part of the Mock module, side_effect allows other cases including raising exceptions
- mock provides a patch() decorator that handles patching module and class level attributes

## The patch() decorator
- the patch() decorator / context manager makes it easy to mock classes or objects in a module under test
- object specified is replaced with a mock (or other object) during the test and restored when it ends
- make it easy to temporarily replace classes in a particular module with a Mock object
    * by default, patch() will create a MagicMock for you
- replaces real objects in code with Mock instances

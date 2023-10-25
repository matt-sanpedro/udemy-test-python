from unittest.mock import Mock

mock = Mock()
print(type(mock))
print(mock)

"""
Lazy Attributes and Methods
- a Mock must simulate any object it replaces, creates attributes when accessed
"""
print(mock.some_attribute)
print(mock.do_something())

"""
If mocking from json library and calling dumps():
- Python mock object will create the method so its interface can match library's interface
- unlike real dumps, mocked method requires no arguments but can accept arguements passed to it
- return value of dumps() is also a Mock, thus return value of mocked method can be used in many ways
"""
json = Mock()
print("JSON dumps: ", json.dumps())

"""
Key Points: 
1. Unlike real dumps() the mocked method requires no arguments, it will accept any arguments
2. Return value of dumps() is also a Mock, capability of Mock to recursively define other mocks
    allows you to use mocks in complex situations
"""
print("JSON loads: ", json.loads("{'k': 'v'}").get('k'))
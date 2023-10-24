"""
Assertions and Inspection
- Mock instances store data on how it's used
    * if you called a method
    * how you called the method
"""
from unittest.mock import Mock

# create mock object
json = Mock()
expected = json.loads("{'key': 'value'}")
print("EXPECTED: ", expected)

# having just called loads(), can make assertions to test expectation
print(json.loads.assert_called()) # ensures the method was called
print(json.loads.assert_called_once())
print(json.loads.assert_called_with("{'key': 'value'}"))
print(json.loads.assert_called_once_with("{'key': 'value'}"))

# calling the loads method again
json.loads("{'key': 'value'}")

# if assertion fails, the mock will raise AssertionError
# OUTPUT: AssertionError: Expected 'loads' to have been called once. Called 2 times.
# print(json.loads.assert_called_once()) 

# OUTPUT: AssertionError: Expected 'loads' to not have been called. Called 2 times.
# print(json.loads.assert_not_called())

# viewing special attributes to understand how application used an object
print("CALL COUNT: ", json.loads.call_count)
# last loads() call
print(json.loads.call_args)
# list of loads() calls
print(json.loads.call_args_list)
# list of calls to json's methods (recursively)
print(json.method_calls)

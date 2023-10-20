# has no info on what folder it is in, cannot perform relative import
# from .libs import mylib

# below import also works
# from libs.operations import operator

from libs import mylib

def divide(dividend, divisor):
    return dividend / divisor

# __name__ is a global variable that changes depending on what file you are running
# "__" can be pronounced as "dunder"
print("mymodule.py: ", __name__)

import libs.mylib
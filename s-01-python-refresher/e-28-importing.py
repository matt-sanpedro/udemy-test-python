from mymodule import divide
import sys

print(divide(10, 2))
print(__name__)

# 1st path: where current python file is executed
# 2nd path: python path
# print(sys.path)

# check what is imported
print(sys.modules)

"""
Notes on exporting paths depending on OS

UNIX:
export PYTHONPATH=/Users

WINDOWS:
set 
"""

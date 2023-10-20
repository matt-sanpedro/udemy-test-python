print("operator.py: ", __name__)

# access the parent folder
# * means "import everything", so all variables, functions, and classes defined inside
# ..my lib will be available as local variables, functions, and classes

# nothing additional will get printed below, python realizes this has already been imported
from ..mylib import *

"""
NOTES
- list and tuples keep order
- sets do NOT keep order but are useful for storing unique values
- lists and tuples use indices for the elements stored
"""

# list: can add/remove elements
l = ["Bob", "Ingrid", "Alexandra"]

# tuple: cannot modify it
t = ("Bob", "Ingrid", "Alexandra")

# set: cannot have duplicates
s = {"Bob", "Ingrid", "Alexandra"}

# below lines do NOT work
# print(s[0])
# s[0] = "LeShon"

# can reassign indice values in lists
l[0] = "LeShonda"
print(l)

# lists add an element
l.append("Karla")
l.remove("Ingrid")
print(l)

# can ADD elements to set: notice add vs append [adds to end of list but sets are unordered]
s.add("Ana")
print(s)

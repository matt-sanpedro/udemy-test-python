# mutable: can change after created
# example: the lists a through d defined below can be changed after defined

# NOTES
# IMMUTABLE in Python: tuples, strings, integers, floats, and booleans
# immutable class can be created, just do NOT add methods in them that can change properties

# a and b are names of the same object, the value is "[]"
a = []
b = a

# the ids printed below are the same
print("a: ", id(a))
print("b: ", id(b))

# appending 77 to a will change both a and b
a.append(77)
print(a)
print(b)

# as a comparison, c and d are initialized each with empty list and are stored separately
# the ids printed below are NOT the same
c = []
d = []
print("c: ", id(c))
print("d: ", id(d))
c.append(15)
print(c)
print(d)

# tuples are immutable
# example: tuple e gets recreated when concatenating as edivent by the ids
e = ()
print("e: ", id(e))
f = ()
e = e + (15,)
print("e: ", id(e))

# h and g are integers with equal values
g = 8597
h = 8597
print("g: ", id(g))
print("h: ", id(h))
g = 8598
print("g: ", id(g))
print("h: ", id(h))

# i and j
i = "hello"
print(i)
j = i
print("i: ", id(i))
print("j: ", id(j))
# reassign i to a new string
i += "world"
print(i)

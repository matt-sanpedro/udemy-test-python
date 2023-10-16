# advanced set topics
friends = {"Bob", "Ingrid", "Alexandra"}
abroad = {"Bob", "Ingrid", "Ana"}

# difference function
local_friends = friends.difference(abroad)
print(local_friends)

abroad_friends = abroad.difference(friends)
print(abroad_friends)

# can initialize empty set
empty_set = set()
print(empty_set)

# school class example
art = {"Bob", "Jen", "Rolf", "Charlie"}
science = {"Bob", "Jen", "Ana", "Alexandra"}

both = art.intersection(science)
print(both) # {"Bob", "Jen"}

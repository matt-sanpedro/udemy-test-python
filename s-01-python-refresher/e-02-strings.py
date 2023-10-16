# f-strings allow us to embed variables in strings
name = "Matt"
greeting = f"Hello, {name}"
print(greeting)

# template strings with .format
greeting = "Hello, {}"
with_name = greeting.format(name)
print(with_name)

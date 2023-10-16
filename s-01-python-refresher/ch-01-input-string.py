# ask user for age
age = int(input("How old are you (years): "))

# create print template
printTemplate = "Your age {}, is equal to {} {} old."

# tell user how many months
toMonths = age * 12
print(printTemplate.format(age, toMonths, "months"))

# tell user how many seconds
toSeconds = toMonths*365*24*3600
print(printTemplate.format(age, toSeconds, "seconds"))

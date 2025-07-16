# A string can be represented with single or double quotes.
language_name = "Python Language"
print(language_name)

# To find lenghth of a string use len()
print(len(language_name))


# To access characters in a string, use indexing. In python, indexing starts at 0.
print(language_name[0])

# To access the last character, use negative indexing.
print(language_name[-1])

# Below example will throw index error as given string is having only max of 15 characters.
# print(language_name[16])  # Slicing from index 0 to 5

# Below will print characters from index 0 to 5 (not including 6).
print(language_name[0:6])

# To convert the string to uppercase, use the upper() method.
print(language_name.upper())

# To convert the string to lowercase, use the lower() method.
print(language_name.lower())

# Return the index of the first occurrence of a substring.
print(language_name.index("Language"))

# Return the index of the first occurrence of a substring. If given substring is not found, it will return -1.
print(language_name.find("Language1"))


language_name = language_name.replace(
    "Python", "Java")  # Replace "Python" with "Java"
print(language_name)


fruits = "apple, banana, cherry"
print("Before Split:", fruits)
# Split the string into a list of fruits

fruits = fruits.split(",")  # Split the string into a list of words
print("After Split:", fruits)


# Formatted String

first_name = "John"
last_name = "Doe"

full_name = f"{first_name} {last_name}"  # Using f-string for formatting
print("Formatted Name:", full_name)


# To strip whitespace from the beginning and end of a string, use the strip() method.

home_address = "  123 Main St, Springfield      "

print("Formatted Address Before Strip:", home_address)

home_address = home_address.strip()

print("Formatted Address After Strip:", home_address)

# IN operator will return a boolean if given substring is available in the given string.
print("pro" in home_address)

print("123" in home_address)

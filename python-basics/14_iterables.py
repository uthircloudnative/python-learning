# In python complex data types like strings, lists, tuples, and dictionaries are considered iterables.
# You can iterate over these data types using loops.

# Example with a string
language_name = "Python Language"

for x in language_name:
    print(x)

# Example with a list
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)


# Example with a tuple
numbers = (1, 2, 3, 4, 5)
for number in numbers:
    print(number)


# Example with a dictionary
person = {"name": "John", "age": 30, "city": "New York"}

for key, value in person.items():
    print(f"{key}: {value}")

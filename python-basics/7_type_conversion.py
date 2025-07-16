# This will receive an input from user.
# In python any input from user is considered as string.
x = input("Enter a number: ")

print(type(x))

# This will result in error as we are trying to add a string to an integer.
# y = x + 1

# We are converting x string to integer before adding 1.
y = int(x) + 1

print("Result after type conversion:", y)

# function definition
def greet():
    print("Hello, Welcome to Python Basics!")
    print("Let's start learning Python functions.")


greet()

# function with parameters


def get_greeting(first_name, last_name):
    return f"Hello, {first_name} {last_name}! Welcome to Python Basics."


message = get_greeting("John", "Doe")
print(message)

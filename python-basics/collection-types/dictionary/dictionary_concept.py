"""
dictionary is key-value type of objects. 
You can use keys to access values in a dictionary.

In disctionaries, keys are unique. If you try to add a key that already exists, the value for that key will be updated.
In Python, dictionaries are defined by enclosing key-value pairs in curly braces {} or by using the dict() constructor.
In dictionaries, keys must be of an immutable data type (like strings, numbers, or tuples), while values can be of any data type.


"""

if __name__ == "__main__":

    # Below definition will create an empy disctionary with name person
    person = {}

    # <class 'dict'> above will create a dictionary object
    print(type(person))

    # <class 'dict'> above will create a dictionary object
    people = dict()
    print(type(person))

    person = {"name": "John", "age": 30, "city": "New York"}

    print("Persopn dictionary :", person)

    size_of_person_dict = len(person)
    print("Size of person dictionary :", size_of_person_dict)

    key_list = list(person) # Converting dictionary keys to a list
    print("Keys in person dictionary returned as list here:", key_list)

    # Access values using keys
    name = person["name"]
    print("Name from person dictionary :", name)

    age = person["age"]
    print("Age from person dictionary :", age)

    # When you try to access a key that does not exist in the dictionary, it will raise a KeyError.
    #country = person["country"]
    #print("Country from person dictionary :", country)

    # To avoid KeyError, you can use the get() method, which returns None if the key does not exist.
    country = person.get("country")
    print("Country from person dictionary using get() method:", country)

    # You can also provide a default value to return if the key does not exist.
    country = person.get("country", "No Key with name country defined in person dictionary")
    print("Country from person dictionary using get() method with default value:", country)

    # Adding a new key-value pair to the dictionary
    person["country"] = "USA"
    print("Updated person dictionary after adding country key:", person)

    # To delte a key-value from dictionary use del keyword. 
    # This will remove the key age and its value from person dictionary
    # If the key does not exist, it will raise a KeyError.
    del person["age"]
    print("Updated person dictionary after deleting age key:", person)

    if "name" in person:
        print("name key is present in person dictionary")
    else:
        print("name key is not present in person dictionary")

    if "zip" not in person:
        print("There is no key with name zip in person object")
    else:
        print("There is a key with name zip in person object")

    # Iterating over dictionary keys
    for key in iter(person):
        print(key)

    for key in person.keys():
        print(key)

    # Iterating over dictionary values
    for value in person.values():
        print(value)

    # Iterating over dictionary key-value pairs
    # Here item will be a tuple of (key, value)
    for item in person.items():
        print(item)

    for key, value in person.items():
        print(f"Key: {key}, Value: {value}")

    # To remove an item and get the valie for removed item use pop() method
    country_value = person.pop("country")
    print("Removed country key value using pop() method:", country_value)
    print("Person dictionary after removing country key using pop() method:", person)

    # To remove and return an arbitrary key-value pair from the dictionary, use popitem() method
    key_value_pair = person.popitem()
    print("Removed arbitrary key-value pair using popitem() method:", key_value_pair)
    print("Person dictionary after removing arbitrary key-value pair using popitem() method:", person)
    

    # Clear all items from the dictionary using clear() method
    person.clear()
    print("Person dictionary after clearing all items using clear() method:", person)

    person = {"name": "John", "age": 30, "city": "New York"}

    print("Person dictionary before copying:", person)

    for key in reversed(person):
        print(key)
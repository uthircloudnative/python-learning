"""
In Python lists are defined by enclosing elements in square brackets [] or by using the list() constructor.
Lists are ordered collections that can hold a variety of data types, including other lists.
Lists are mutable, meaning their elements can be changed after the list is created.
Lists allow duplicate elements.
Lists are homogeneous, meaning they can contain elements of different data types.


"""


if __name__ == "__main__":

    fruits = ["apple", "banana", "cherry"]
    print("Fruits in List :", fruits)

    size_of_fruits_list = len(fruits)
    print("Size of fruits list :", size_of_fruits_list)

    # List supports index based access.
    first_fruit = fruits[0]
    print("First fruit from fruits list :", first_fruit)

    last_fruit = fruits[-1]
    print("Last fruit from fruits list :", last_fruit)

    second_last_fruit = fruits[-2]
    print("Second last fruit from fruits list :", second_last_fruit)

    # Adding an element to the list using append() method
    fruits.append("orange")
    print("Fruits list after adding an element :", fruits)

    # Printing lenght of the list after adding an element
    size_of_fruits = len(fruits)
    print("Size of fruits list after adding an element :", size_of_fruits)

    # Removing a given specific element from list using remove() method.
    fruits.remove("banana")
    print("Fruits list after removing an element :", fruits)

    # pop() method will remove the last eleent from the list
    # If list is empty then it will raise an IndexError.
    removed_fruit = fruits.pop()
    print("Removed fruit using pop() method :", removed_fruit)
    print("Fruits list after removing last element using pop() method :", fruits)

    some_more_fruits = ["mango", "grape", "kiwi", "apple"]

    # To add 2 list we can use extend() method
    fruits.extend(some_more_fruits)
    print("Fruits list after extending with some_more_fruits :", fruits)

    # To count number of occurance of an element in the list we can use count() method
    apple_count = fruits.count("apple")
    print("Number of occurance of apple in fruits list :", apple_count)

    abc_count = fruits.count("abc")
    print("Number of occurance of abc in fruits list :", abc_count)

    # To find index of an element in the list we can use index() method
    mango_index = fruits.index("mango")
    print("Index of mango in fruits list :", mango_index)

     # If the element is not present in the list, it will raise a ValueError.
    apple_index = fruits.index("apple")
    print("Index of apple in fruits list :", apple_index)

    # To sort the list we can use sort() method
    fruits.sort()
    print("Fruits list after sorting :", fruits)

    # To remove a specici index element we can using pop([0])
    first_fruit = fruits.pop(0)
    print("First fruit removed using pop(0) method :", first_fruit)
    print("Fruits list after removing first element using pop(0) method :", fruits)

    # To reverse the list we can use reverse() method
    fruits.reverse()
    print("Fruits list after reversing :", fruits)

    # Inserting an element at specific index using insert() method  
    fruits.insert(1, "blueberry")
    print("Fruits list after inserting blueberry at index 1 :", fruits)

    # Slicing the list to get a sublist
    sublist_fruits = fruits[1:4]
    print("Sublist of fruits from index 1 to 3 :", sublist_fruits)

    # Iterating over the list elements

    for fruit in fruits:
        print(fruit)




   

"""
Set is Unordered collection of unique elements.
In Python, sets are defined by enclosing elements in curly braces {} or by using the set() constructor.
Sets are mutable, meaning you can add or remove elements after the set has been created.
Sets are Hertogeneous, meaning they can contain elements of different data types.
Example:
# Creating a set
my_set = {1,2,"apple", True, 3.14} This set contains different data types. Its valid and considered as hetrogenous set.
# Creating a set using set() constructor
another_set = set([1, 2, 3, 4, 5])

In Sets, duplicate elements are automatically removed.

# Example of duplicate elements in a set
my_set = {1, 2, 2, 3, 4, 4}
print(my_set)  # Output: {1, 2, 3, 4}
"""


if __name__ == "__main__":
    # Create a set with duplicate elements.
    marks = {90, 80, 75, 28, 90, 80}
    
    # Marks in Set: {80, 90, 75, 28}
    print("Marks in Set:", marks)

    # Create a set using set() constructor with duplicate elements.
    scores = set([90, 80, 75, 28, 90, 80])

    # Scores in Set: {90,80, 75, 28}
    print("Scores in Set:", scores)

    scores.add(71)

    # Scores in Set: {90,80, 75, 28, 71}
    print("Scores in Set:", scores)

    # Length of a Set
    print("Length of Scores Set:", len(scores))

    if 75 in scores:
        print("75 is present in the scores set")
    else:
        print("75 is not present in the scores set")

    if 100 not in scores:
        print("100 is not present in the scores set")
    else:
        print("100 is present in the scores set")

    # When we have 2 set a and b to check ecah and every element in b is there in a use issubset({set})
    fruits = {"apple", "banana", "cranberry"}

    eatables = {"rice", "apple", "chicken", "banana", "cranberry"}

    # eatables conatins all the fruits
    if fruits.issubset(eatables) :
        print("eatables conatins all the fruits")
    else:
        print("eatables not conatins all the fruits")

    # When we have 2 set a and b to check ecah and every element in a is there in b use issuperset({set})
    if eatables.issuperset(fruits) :
        print("eatables conatins all the fruits")
    else:
        print("eatables not conatins all the fruits")

    # Union of 2 sets - To combines 2 set and removes duplicate elements use union({set}) or | operator
    male_ages = {25, 30, 22, 28, 18}
    female_age = {24, 27, 22, 26, 18}

    all_ages = male_ages.union(female_age)
    # {25, 30, 22, 28, 18, 24, 27, 26}
    print("All ages :", all_ages)

    all_ages = male_ages | female_age # This is equivalent to union
    # {25, 30, 22, 28, 18, 24, 27, 26}
    print("All ages :", all_ages)

    # intersection will give common elements as result between 2 sets.
    all_ages = male_ages.intersection(female_age)

    # {22, 18}
    print("All ages :", all_ages)
    print("All ages :", (male_ages & female_age))

    
    male_different_ages = male_ages.difference(female_age)

    # {25, 30, 28}
    print("Male different Ages :", male_different_ages)

    female_different_ages = female_age.difference(male_ages)

    # {24, 27, 26}
    print("Female different Ages :", female_different_ages)

    symmetric_difference_age = male_ages.symmetric_difference(female_age)

    # Ages which is not common in male_ages and female_age sets. {25, 30, 28, 24, 27, 26} 
    print("symmmetric_difference ages :", symmetric_difference_age)

    male_ages.add(35)

    # Set.add will add the given element to the set.
    # {25, 30, 22, 28, 18, 35}
    print("Male ages after adding 35 :", male_ages)

    # set.remove() will remove the given element from the set.
    # If the given element is not present in the set, it will raise a KeyError.
    # {25, 30, 28, 18, 35}
    male_ages.remove(22)

    print("Male ages after removing 22 :", male_ages)

    # male_ages.remove(100) # This will raise KeyError as 100 is not present in the set.

    # set.discard() will remove the given element from the set.
    # If the given element is not present in the set, it will NOT raise any error
    male_ages.discard(18)

    print("Male ages after discarding 18 :", male_ages)

    male_ages.discard(18)

    print("Male ages after discarding 18 :", male_ages) # No error raised as 18 is not present in the set.

    # set.pop() will remove and return an arbitrary element from the set. If the set is empty, it will raise a KeyError.
    poped_age = male_ages.pop()
    print("Poped age :", poped_age)
    print("Male ages after poping :", male_ages)

    # Shallow copy of a set can be created using set.copy() method.
    
    male_ages_copy = male_ages.copy()

    print("Male ages original set :", male_ages)
    print("Male ages copy set :", male_ages_copy)

    print("Memory address of male_ages :", id(male_ages))
    print("Memory address of male_ages copy :", id(male_ages_copy))

    male_ages.clear()

    print("Male ages after clearing :", male_ages)
    print("Male ages after clearing :", len(male_ages))
    print("Male ages copy after clearing  male_ages:", male_ages_copy)
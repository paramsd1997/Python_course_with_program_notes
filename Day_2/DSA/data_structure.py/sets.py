""" set properties
Unordered: Sets do not maintain the order of elements.

Mutable: Sets can be modified by adding or removing elements.

Unique Elements: Sets contain only unique elements; duplicate values are automatically removed.

Heterogeneous: Sets can hold elements of different data types.

No Indexing: Elements in a set are not accessible by index.

Mathematical Operations: Sets support mathematical set operations like union, intersection, and difference.

Used for Uniqueness: Sets are often used to ensure the uniqueness of elements in a collection.
    
    
    """

#  Creating a Set:
#You can create a set by listing its elements inside curly braces {}:

my_set = {1, 2, 3, 4, 5}
print(my_set)

# Union (|): Combines elements from two sets, excluding duplicates.
# Intersection (&): Finds elements common to both sets.
# Difference (-): Finds elements that are unique to one set.
# add(): Adds an element to the set.
# remove() :  Removes a specific element from the set.
# clear(): Removes all elements from the set, leaving an empty set.
# 


set1 = {1, 2, 3}
set2 = {3, 4, 5}

union_set = set1 | set2  # Union: {1, 2, 3, 4, 5}
intersection_set = set1 & set2  # Intersection: {3}
difference_set = set1 - set2  # Difference: {1, 2}

my_set.add(100) # it will add the 100
print(my_set)

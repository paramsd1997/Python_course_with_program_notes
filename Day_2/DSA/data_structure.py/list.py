# Working with lists in Python is fundamental as they are versatile and widely used for storing and manipulating collections of data. 

"""Ordered: Lists maintain the order of elements as they are added.
Mutable:    Lists can be modified by adding, removing, or changing elements.
Allows Duplicates: Lists can contain duplicate elements.
Heterogeneous: Lists can hold elements of different data types.
Indexed: Elements in a list are accessible by their index (position).
Iterative: You can loop through the elements of a list using loops like for.
Common Operations: Lists support various operations, such as appending, removing, slicing, and sorting.
"""

# To create a list in Python, enclose a comma-separated sequence of values in square brackets []
list1 = [1, 2, 3, 4, 5]
print(list1)

list1.append(6)
print(list1)

# length 
len(list1)
print(len(list1))


# Slicing Lists:
# Slicing allows you to extract a portion of a list. 
# You specify a start and end index to create a new list containing the selected elements:

list1 = [1, 2, 3, 4, 5]
sliced_list = list1[1:4]  # Slices elements at index 1, 2, and 3
print(sliced_list)  # Prints [2, 3, 4]


# Modifying List Elements:
# You can change the value of an element by assigning a new value to it using indexing:
list1 = [1, 2, 3, 4, 5]
list1[2] = 10
print(list1)  # Prints [1, 2, 10, 4, 5]

# To remove elements from a list, you can use methods like remove() to remove a specific value or pop() to remove an element by index:
list1 = [1, 2, 3, 4]
list1.remove(3)  # Removes the value 3
print(list1)  # Prints [1, 2, 4]

popped_value = list1.pop(1)  # Removes and returns the element at index 1 (2)
print(list1)  # Prints [1, 4]
print(popped_value)  # Prints 2


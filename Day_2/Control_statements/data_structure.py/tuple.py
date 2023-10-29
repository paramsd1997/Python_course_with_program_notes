"""
Tuple properties in Python, in short, include:

1. **Ordered:** Tuples maintain the order of elements as they are added.

2. **Immutable:** Tuples cannot be changed after creation, meaning you can't add, remove, or modify elements.

3. **Allows Duplicates:** Tuples can contain duplicate elements.

4. **Heterogeneous:** Tuples can hold elements of different data types.

5. **Indexed:** Elements in a tuple are accessible by their index (position).

6. **Iterative:** You can loop through the elements of a tuple using loops like `for`.

7. **Used for Data Integrity:** Tuples are often used to ensure the integrity of data that should not be modified.
"""

# To create a list in Python, enclose a comma-separated sequence of values in square brackets ()
my_tuple = (55, "hey", 3.8, 4, 5)
print(my_tuple)

#Accessing Tuple Elements (Indexing):
# You can access individual elements of a tuple using their index, just like with lists. Indexing starts at 0 for the first element:

print(my_tuple[0])  # Prints 1 (the first element)
print(my_tuple[2])  # Prints 3 (the third element)



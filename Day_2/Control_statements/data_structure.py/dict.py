"""
Unordered: Dictionaries do not maintain the order of elements.

Key-Value Pairs: Dictionaries consist of key-value pairs, where each key is associated with a value.

Mutable: You can add, remove, or modify key-value pairs in a dictionary.

Keys are Unique: Keys within a dictionary must be unique; there cannot be duplicate keys.

Heterogeneous Values: Dictionary values can be of different data types.

Indexed by Keys: Elements are accessed by their keys rather than by index.

Iterative: You can iterate through keys, values, or key-value pairs using loops or methods.
    """
    
    
    # Creating a Dictionary:

# You can create a dictionary by enclosing key-value pairs in curly braces {}. 
# Each pair consists of a key and its associated value, separated by a colon :.
my_dict = {"name": "John", "age": 30, "city": "New York"}
print(my_dict)

## Accessing the keys & values

keys = my_dict.keys()        # Returns a list of keys
values = my_dict.values()    # Returns a list of values
print("all keys : ",keys)
print("all values are :",values)

# deleting the values
my_dict.pop("city")
print(my_dict)

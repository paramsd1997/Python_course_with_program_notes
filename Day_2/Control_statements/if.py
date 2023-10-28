# if Statement:
""" The if statement is used to execute a block of code if a given condition is True.
 If the condition is False, the code block is skipped. """
 
x = 10
if x > 5:
 print("x is greater than 5")
else:
     print("x is less than 5")
     
     
""" else Statement:
The else statement is used to define a block of code to be executed if none of the previous conditions 
(in if and elif) is True."""
x = 3
if x > 5:
    print("x is greater than 5")
else:
    print("x is not greater than 5")
    
    """elif Statement:
The elif statement stands for "else if" and is used to test multiple conditions. 
You can have multiple elif statements after an if statement. 
If the if condition is False, the program checks the elif conditions one by one until it finds one that is True, and the corresponding block of code is executed. 
If none of the conditions is True, the code block under the else statement (if present) will be executed.
    """
    x = 10
if x > 15:
    print("x is greater than 15")
elif x > 5:
    print("x is greater than 5 but not greater than 15")
else:
    print("x is not greater than 15 or 5")


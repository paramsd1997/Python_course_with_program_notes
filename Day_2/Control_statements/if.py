# if Statement:
""" The if statement is used to execute a block of code if a given condition is True.
 If the condition is False, the code block is skipped. """

x = 100
if x > 500:
 print("just say yes ")
else:
     print("or else No")













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
    x = 5000

if x > 10000:
    print("yes it greater than 1000")

elif x > 2000:
    print("yes it greater than 2000")

else:
    print("hey bro conditions is not true ")


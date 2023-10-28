# break: Terminates the loop prematurely.
# continue: Skips the current iteration and proceeds to the next.

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    if fruit == "banana":
        break  # Exit the loop when "banana" is encountered
    if fruit == "cherry":
        continue  # Skip "cherry" and move to the next iteration
    print(fruit)
else:
    print("Loop completed normally.")

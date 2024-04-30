# Prompt the user to input a camelCase string.
camelcase = input("camelCase: ")

# Print the beginning of the snake_case string.
print("snake_case: ", end="")

# Iterate through each character in the camelCase string.
for c in camelcase:
    # Check if the character is lowercase.
    if c.islower():
        # If the character is lowercase, simply print it.
        print(c, end="")
    else:
        # If the character is uppercase, print an underscore followed by its lowercase equivalent.
        print("_" + c.lower(), end="")

# Print a newline character to end the snake_case string.
print("")

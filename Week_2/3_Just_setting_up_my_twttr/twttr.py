# Prompt the user to input a string.
input_text = input("Input: ")

# Iterate through each character in the input string.
for c in input_text:
    # Check if the character is a vowel (either lowercase or uppercase).
    if c in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
        # If it's a vowel, print nothing (skip printing).
        print("", end="")
    else:
        # If it's not a vowel, print the character.
        print(c, end="")

# Print a newline character to end the line.
print("")

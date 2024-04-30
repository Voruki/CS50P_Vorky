# Prompt the user to input their answer to the Great Question of Life, the Universe, and Everything.
input_text = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")

# Remove spaces from the input and convert it to lowercase for case-insensitive comparison.
new_input = input_text.replace(" ", "").lower()

# Check if the input matches any of the accepted answers: "42", "forty-two", or "fortytwo".
if new_input == "42" or new_input == "forty-two" or new_input == "fortytwo":
    # If the input matches, print "Yes".
    print("Yes")
else:
    # If the input does not match, print "No".
    print("No")

# Prompt the user to input a greeting.
input_text = input("Greeting: ")

# Remove spaces from the input and convert it to lowercase for case-insensitive comparison.
new_input = input_text.replace(" ", "").lower()

# Check if "hello" is in the input text.
if "hello" in new_input:
    # If "hello" is present, print "$0".
    print("$0")
# Check if the input starts with the letter "h".
elif "h" == new_input[0]:
    # If the input starts with "h", print "$20".
    print("$20")
else:
    # If none of the above conditions are met, print "$100".
    print("$100")

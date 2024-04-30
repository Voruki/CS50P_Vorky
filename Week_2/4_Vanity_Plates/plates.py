# Define the main function.
def main():
    # Prompt the user to input a license plate number.
    plate = input("Plate: ")
    
    # Check if the input plate is valid using the is_valid function.
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

# Define the is_valid function to check if the license plate number is valid.
def is_valid(s):
    # Check if the length of the string is between 2 and 6 characters, inclusive,
    # and the first two characters are alphabetic.
    if 6 >= len(s) >= 2 and s[0:2].isalpha() and s.isalnum():
        # Iterate through each character in the string.
        for char in s:
            # Check if the character is a digit.
            if char.isdigit():
                # Get the index of the first digit character.
                index = s.index(char)
                # Check if all characters after the first digit are digits,
                # and the digit character is not at the beginning of the string.
                if s[index:].isdigit() and char != '0':
                    return True
                else:
                    return False
        # If no invalid conditions are found, return True.
        return True

# Call the main function to start the program.
main()

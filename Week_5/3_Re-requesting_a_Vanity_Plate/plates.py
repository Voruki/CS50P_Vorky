import sys

def main():
    # Prompt the user to enter a name.
    user_input = input("Enter Name: ")
    # Check if the input name is valid.
    if is_valid(user_input):
        print("valid")
        # Exit the script with a success status code.
        sys.exit(0)
    else:
        print("invalid")
        # Exit the script with a failure status code.
        sys.exit(1)

# Function to check if the length of the input string is between 2 and 6 characters.
def check_len_input(a):
    if len(a) > 6 or len(a) < 2:
        return False
    return True

# Function to check if the input string meets various validation criteria.
def is_valid(input_string):
    # Check if the length of the input string is valid.
    if check_len_input(input_string) != True:
        return False

    # Check if the first two characters are alphabetic.
    if not input_string[0].isalpha() and not input_string[1].isalpha():
        return False

    # Iterate through the input string to check for numeric characters.
    counter = 0
    while counter < len(input_string):
        if input_string[counter].isdigit():
            # If a digit is encountered, check if it's not '0'.
            if input_string[counter] == '0':
                return False
            else:
                break
        counter = counter + 1

    # Check if the input string contains any punctuation or space characters.
    for each in input_string:
        if each in ['.', '!', '?', ' ']:
            return False

    # Iterate through the input string to check if the characters after the first numeric character are all numeric.
    for i, c in enumerate(input_string):
        if c.isdigit():
            temp = input_string[i:]
            # If characters after the first numeric character are found, check if they are all numeric.
            if is_number(temp) != True:
                return False
            else:
                break
    return True

# Function to check if a string consists entirely of numeric characters.
def is_number(s):
    for each in s:
        if each.isdigit() == False:
            return False
    return True

# Check if the script is executed directly, and if so, call the main function.
if __name__ == "__main__":
    main()

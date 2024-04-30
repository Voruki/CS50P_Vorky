def main():
    # Call the shorten function with the string "twitter" and print the result.
    answer = shorten("twitter")
    print(answer)

# Define the shorten function to remove vowels from a given string.
def shorten(str_in):
    # Iterate through each character in the input string.
    for each in str_in:
        # Check if the character is a vowel (both uppercase and lowercase).
        if each.upper() in ['A', 'E', 'I', 'O', 'U']:
            # If the character is a vowel, replace it with an empty string.
            str_in = str_in.replace(each, "")
    # Return the modified string without vowels.
    return str_in

# Check if the script is executed directly, and if so, call the main function.
if __name__ == "__main__":
    main()

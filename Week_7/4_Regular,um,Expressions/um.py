import re

def main():
    # Take input from the user
    print(count(input("Text: ")))

def count(s):
    # Define the regex pattern to match the word "um" with optional non-word characters before and after
    regex = "(^|\W)um($|\W)"
    # Use findall to search for all occurrences of the word "um" in the input string, ignoring case
    match = re.findall(regex, s, re.IGNORECASE)
    if match:
        # Return the count of matches found
        return len(match)

if __name__ == "__main__":
    main()

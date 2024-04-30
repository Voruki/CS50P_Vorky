def main():
    # Prompt the user to input a greeting.
    in_user = input("Greeting: ")
    # Call the value function to determine the value of the greeting.
    answer = value(in_user)
    # Print the value of the greeting with a dollar sign.
    print(f"${answer}")

def value(str_in):
    # Check if the input string starts with "hello" (case insensitive).
    if str_in.lower().startswith("hello"):
        # If the input starts with "hello", return a value of 0.
        return 0
    # Check if the first character of the input (after converting to lowercase) is 'h'.
    elif str_in[0].lower() == 'h':
        # If the first character is 'h', return a value of 20.
        return 20
    else:
        # If none of the above conditions are met, return a default value of 100.
        return 100

# Check if the script is executed directly, and if so, call the main function.
if __name__ == "__main__":
    main()

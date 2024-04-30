def main():
    # Prompt the user to input a value.
    user_input = input("Here: ")
    # Convert the user input to a percentage.
    user_input = convert(user_input)
    # Print the gauge representation based on the percentage.
    print(gauge(user_input))

# Function to determine the gauge representation based on the percentage.
def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return str(percentage) + "%"

# Function to convert the user input to a percentage.
def convert(user):
    while True:
        try:
            # Split the user input into two parts separated by a "/".
            one, two = user.split("/")
            # Convert the parts to integers.
            one = int(one)
            two = int(two)
            # Check if the first part is greater than the second part.
            if one > two:
                # If so, ask for input again.
                continue
        except ValueError:
            # If the input cannot be split into two parts or converted to integers, raise an error.
            raise
        else:
            try:
                # Calculate the percentage.
                result = (one / two) * 100
                # Round the result to the nearest integer.
                result = round(result)
                # Convert the result to an integer.
                result = int(result)
            except ZeroDivisionError:
                # If there's a division by zero error, raise an error.
                raise
            else:
                # If everything is successful, return the result.
                return result

if __name__ == "__main__":
    main()

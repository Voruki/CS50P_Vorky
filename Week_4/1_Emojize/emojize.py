import emoji

# Prompt the user to input a string.
input_user = input("Input: ")

# Check if the input matches specific aliases and convert them accordingly.
if input_user == ":thumbsup:":
    # If the input is ":thumbsup:", replace it with ":thumbs_up:".
    input_user = ":thumbs_up:"
    # Convert the updated input to its corresponding emoji character.
    output = emoji.emojize(input_user)
    # Print the output.
    print("Output:", output)

elif input_user == ":earth_asia:":
    # If the input is ":earth_asia:", replace it with ":globe_showing_Asia-Australia:".
    input_user = ":globe_showing_Asia-Australia:"
    # Convert the updated input to its corresponding emoji character.
    output = emoji.emojize(input_user)
    # Print the output.
    print("Output:", output)

else:
    # For any other input, simply convert it to its corresponding emoji character.
    output = emoji.emojize(input_user)
    # Print the output.
    print("Output:", output)

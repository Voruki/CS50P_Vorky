import random

# Define the main function to run the game.
def main():
    # Prompt the user to input the level (the maximum possible value of the random number).
    input_user = valid_input("Level: ")
    
    # Generate a random number between 0 and the user input value.
    rand_number = random.randint(0, input_user)

    # Start the game loop.
    while True:
        # Prompt the user to input their guess.
        user = valid_input("Guess: ")
        
        # Check if the user's guess matches the random number.
        if user == rand_number:
            print("Just right!")
            break
        # If the user's guess is smaller than the random number, provide feedback.
        elif user < rand_number:
            print("Too small!")
        # If the user's guess is larger than the random number, provide feedback.
        elif user > rand_number:
            print("Too Large!")

# Define a function to validate user input.
def valid_input(message_in):
    while True:
        try:
            # Prompt the user to input a value and convert it to an integer.
            temp = int(input(message_in))
            # Check if the input is less than or equal to 0.
            if temp <= 0:
                continue
        # Handle the ValueError exception if the input cannot be converted to an integer.
        except ValueError:
            continue
        else:
            # If the input passes all checks, return it.
            return temp

# Run the main function if this script is executed directly.
if __name__ == "__main__":
    main()

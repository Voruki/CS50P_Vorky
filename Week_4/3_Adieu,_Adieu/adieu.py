import inflect

# Initialize the Inflect engine.
engine = inflect.engine()

# Start message.
adieu = 'Adieu, adieu, to'

# Create a list to store names.
names_input = []

# Continuously prompt the user to input names until Ctrl + D is entered.
while True:
    try:
        # Prompt the user to input a name.
        user = input("Name: ")
        # Add each name to the list.
        names_input.append(user)
    # Handle the EOFError exception, which occurs when the user enters Ctrl + D.
    except EOFError:
        print('')
        # Exit the loop.
        break

# Join the names together using the Inflect library.
answer = engine.join(names_input)

# Print the farewell message along with the joined names.
print(adieu, answer)

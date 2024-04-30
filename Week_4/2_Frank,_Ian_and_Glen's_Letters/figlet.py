import random as RAN
import pyfiglet as fig
import sys

# Initialize a Figlet object.
figlet = fig.Figlet()

# Get a list of all available fonts.
fonts = figlet.getFonts()

# Check command line arguments for valid usage.
if len(sys.argv) > 3 or len(sys.argv) > 1 and len(sys.argv) < 3:
    print('Invalid usage')
    sys.exit(1)

# If two command line arguments are provided.
if len(sys.argv) == 3:
    # Extract the font and flag from command line arguments.
    font = sys.argv[2]
    font_flag = sys.argv[1]

    # Check if the specified font is valid.
    if font not in fonts:
        print('Invalid usage')
        sys.exit(1)

    # Check if the flag is valid.
    if font_flag not in ['-f','--font']:
        print('Invalid usage')
        sys.exit(1)

    # Set the font to the specified one.
    figlet.setFont(font=font)

    # Prompt the user to input a string.
    user_input = input("Input: ")
    # Render the input text with the specified font and print it.
    print(figlet.renderText(user_input))
    sys.exit(0)

# If no command line arguments are provided, or if only one argument is provided.
# This branch randomly selects a font and uses it to render the input text.
rand_number = RAN.randint(0,len(fonts)-1)
figlet.setFont(font=fonts[rand_number])
user_input = input("Input: ")
print(figlet.renderText(user_input))
sys.exit(0)

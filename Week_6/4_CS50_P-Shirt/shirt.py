import sys
from PIL import Image, ImageOps

# Allowed extensions for input and output images
allowed_ext = ["png", "jpg", "jpeg"]

# Function to check command-line arguments
def check_command_line():
    if len(sys.argv) != 3:
        sys.exit("Incorrect number of command-line arguments")

# Function to check the extensions of input and output files
def check_arg_extension():
    # Split the input and output file paths and get the extensions
    input_ext = sys.argv[1].rsplit(".")[-1]
    output_ext = sys.argv[2].rsplit(".")[-1]

    # Check if the output extension is allowed
    if output_ext.lower() not in allowed_ext:
        sys.exit(f"{output_ext} is not allowed")

    # Check if the input extension is allowed
    if input_ext.lower() not in allowed_ext:
        sys.exit(f"{input_ext} is not allowed")

    # Check if input and output extensions are the same
    if input_ext.lower() != output_ext.lower():
        sys.exit("Different extensions for input and output files")

# Main function
def main():
    # Check command line arguments
    check_command_line()

    # Check file extensions
    check_arg_extension()

    # Open the shirt image
    try:
        shirt = Image.open("shirt.png")
    except FileNotFoundError:
        sys.exit("Shirt image not found")

    # Open the input image
    try:
        muppet = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("Input image not found")

    # Get the size of the shirt image
    size = shirt.size

    # Resize the input image to fit the size of the shirt
    muppet = ImageOps.fit(muppet, size)

    # Paste the input image onto the shirt image
    muppet.paste(shirt, (0, 0), shirt)

    # Save the output image
    muppet.save(sys.argv[2])

if __name__ == '__main__':
    main()

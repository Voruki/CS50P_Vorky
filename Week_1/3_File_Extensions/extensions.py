# Define the main function to handle the file name input and call the formula function.
def main():
    # Prompt the user to input the file name, convert it to lowercase, and strip whitespace.
    file = input("What is file name? ").casefold().strip()
    
    # Split the file name into three parts: name, part (the period), and extension.
    name, part, ext = file.partition('.')
    
    # Call the formula function with the file extension.
    formula(ext)

# Define the formula function to determine the MIME type based on the file extension.
def formula(x):
    # Match the file extension.
    match x:
        # If the extension is "gif", print the MIME type.
        case "gif":
            print("image/gif")
        # If the extension is "jpg" or "jpeg", print the MIME type.
        case "jpg" | "jpeg":
            print("image/jpeg")
        # If the extension is "png", print the MIME type.
        case "png":
            print("image/png")
        # If the extension is "pdf", print the MIME type.
        case "pdf":
            print("application/pdf")
        # If the extension is "txt", print the MIME type.
        case "txt":
            print("text/plain")
        # If the extension is "zip", print the MIME type.
        case "zip":
            print("application/zip")
        # For any other extension, print the default MIME type.
        case _:
            print("application/octet-stream")

# Call the main function to start the program.
main()

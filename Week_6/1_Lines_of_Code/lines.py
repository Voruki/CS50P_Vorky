import sys

def main():
    # Check command-line argument
    check_command_line_file()

    # Read file and return the number of lines of code in it
    line = read_content(sys.argv[1])
    print(line)

def check_command_line_file():
    # Check the number of command-line arguments
    if len(sys.argv) > 2:
        print("Too many command-line arguments")
        sys.exit(1)
    elif len(sys.argv) < 2:
        print("Too few command-line arguments")
        sys.exit(1)

    # Check if the input file is a Python file
    if ".py" not in sys.argv[1]:
        print("Not a Python file")
        sys.exit(1)

def read_content(FileInput):
    line_counter = 0
    try:
        with open(FileInput, encoding='utf8') as file:
            file_lines = file.readlines()
    except FileNotFoundError:
        print("File Not Found")
        sys.exit(1)

    # Remove all white spaces and comments
    for line in file_lines:
        if line.strip().startswith("#"):  # Ignore lines starting with #
            pass
        elif line.strip() == "":  # Ignore empty lines
            pass
        else:
            line_counter += 1  # Increment line counter for non-empty, non-comment lines
    return line_counter

if __name__ == "__main__":
    main()

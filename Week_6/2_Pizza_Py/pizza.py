import sys
import csv
from tabulate import tabulate

def main():
    # Check command-line arguments
    check_command_line()
    # Read content from CSV file
    read_content(sys.argv[1])

def check_command_line():
    # Check the number of command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Invalid number of command-line arguments")

    # Check if the input file is a CSV file
    if not sys.argv[1].endswith('.csv'):
        sys.exit("Not a CSV file")

def read_content(fileInput):
    header = []
    body = []
    try:
        with open(fileInput, encoding="utf-8") as file:
            reader = csv.reader(file)
            for (index, value) in enumerate(reader):
                # First row contains headers
                if index == 0:
                    header.append(value)
                else:
                    body.append(value)

        # Print table using tabulate
        print(tabulate(body, headers=header[0], tablefmt="grid"))

    except FileNotFoundError:
        sys.exit("File not found")

if __name__ == "__main__":
    main()
